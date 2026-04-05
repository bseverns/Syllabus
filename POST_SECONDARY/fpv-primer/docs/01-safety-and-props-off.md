# Safety and props-off doctrine

## Non-negotiables
- Remove props for bench work. Always.
- Treat batteries as live energy and potential fire risk.
- Power on in a clear area with a plan for “kill power now.”
- Use smoke-stopper / current limiting for first power-ups.
- Do not let “just a quick test” override the ritual.

## Props-off workflow
1. Visual inspection (wires, solder joints, loose screws)
2. Battery connection with restraint + clear cable path
3. Confirm arming is disabled (or motor outputs disabled)
4. Confirm receiver behavior + failsafe
5. Only then: enable motor outputs if needed for verification

## Why this doctrine exists

Props-off bench work is not over-caution. It is what allows you to:

- isolate configuration errors from flight errors
- inspect behavior slowly
- prove receiver and failsafe behavior
- test telemetry and logging without turning every mistake into a physical incident

## Expanded stop rules

Stop immediately if:

- the battery or connector gets unexpectedly hot
- a motor twitches or spins when it should not
- the FC disconnects or reboots repeatedly
- you smell electronics cooking
- the receiver shows unstable behavior you cannot explain
- your test plan becomes vague

## “Stop rules”
Stop immediately if you see:
- smoke, heat, smell
- battery puffing or hot connector
- motors spinning unexpectedly
- runaway behavior in software

This repo assumes you can demonstrate stable, expected behavior on the bench before you ever fly.

## Bench roles that help in teaching

For paired work:

- **operator**: holds the plan, calls the steps
- **observer**: watches for unexpected behavior and writes notes
- **power authority**: the person allowed to connect or disconnect the battery

Making those roles explicit reduces sloppy bench culture fast.
