# GOALS — what this cleanup is steering toward (TEMPLATE)

Copy this into the project being cleaned (its root, or wherever the project keeps its docs) and
edit it to that project's real end states. The cleanup router reads the *project's* `GOALS.md`, not
this template — this file is only the starting suggestion. Update anytime by editing the project's
`GOALS.md`; the router re-reads it every run, so the latest version always frames the work.

This doc describes *destinations*, not defects. Every finding the audit reports names the goal here
it serves, in plain terms; a finding that serves no goal here is noise — say so and drop it. Keep it
calm: one line per thing, no jargon.

## The end state (suggested starting goals — edit freely)

1. **Less clutter.** A workspace I can look at and understand.
2. **A map — I know where everything is.** So I can steer when the agent goes wrong; no guessing
   which copy is real.
3. **Backups I can trust.** A second copy that stays accurate and maintains itself — seamless, not
   a chore.
4. **In sync across devices.** Current and reachable everywhere I work, no conflicted copies.
5. **The right home for each thing — one home per thing.** Each file lives in exactly one place,
   chosen by what it is: cloud sync vs version control vs out-of-sync scratch. No scattering the same
   thing across several homes, no defaulting everything to one place.
6. **Shared components, many consumers — fix once.** Where projects share code or config, a fix
   proven on one propagates to the shared layer so it never re-bites a sibling. A pattern proven on
   one project is the template the next starts from.

## How the skills use this
- The router shows these goals at the start of a run and asks which the run serves.
- The audit ties each finding to the goal it serves.
- The fix skills state which goal a fix advances before doing it.
