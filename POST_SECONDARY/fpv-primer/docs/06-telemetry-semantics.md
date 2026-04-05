# Telemetry semantics (make the invisible consistent)

Define semantics *before* mapping.

If you skip this, your mapping layer will accidentally compose:

- sensor noise
- dropout behavior
- hidden state changes
- misunderstanding

## The questions every signal must answer

- What does this value mean?
- When is it valid?
- What range is normal?
- What does `0` mean?
- What does missing data mean?
- What should happen downstream if the value becomes implausible?

## Example semantic table for an Air65-style ELRS whoop

| Signal | Meaning | Typical raw form | Valid when | Important caveat |
| --- | --- | --- | --- | --- |
| `arm_state` | craft is armed or disarmed | boolean or mode-derived | always | do not confuse armed-idle with active thrust |
| `throttle_cmd` | pilot throttle command | channel value | receiver valid | command is not the same as actual thrust |
| `roll_cmd` | pilot roll command | channel value | receiver valid | center jitter must be handled |
| `pitch_cmd` | pilot pitch command | channel value | receiver valid | sign convention must be documented |
| `yaw_cmd` | pilot yaw command | channel value | receiver valid | often noisy around center without deadband |
| `vbat` | battery voltage | volts or centivolts | battery connected | sag under load is expected, not always a fault |
| `link_quality` | quality of ELRS control link | percent or scaled integer | receiver valid | treat disappearance differently from weak-but-valid |
| `rssi` | signal-strength indicator | scaled value | protocol dependent | often less useful than LQ on ELRS workflows |
| `motor_output_n` | FC command to each motor | motor value | armed or test mode | command is not direct proof of physical motor health |

## Normalization rules

Do not normalize by instinct. State the rule.

Examples:

- RC command range -> `[-1, 1]`
- Battery voltage -> `[0, 1]` based on a chosen safe operating window
- Link quality -> `[0, 1]` with a documented floor and ceiling

Write the transformation explicitly, for example:

```text
normalized = clamp((raw - min_expected) / (max_expected - min_expected), 0, 1)
```

## Failure handling

Choose one behavior per signal and document it:

- **hold last**
- **decay to zero**
- **hard zero**
- **safe default**
- **invalidate downstream output**

There is no universally correct choice. There is only documented choice versus accidental behavior.

## Post-secondary rule

If two students implement different meanings for the same source signal, they are not comparing mappings. They are comparing semantic errors.
