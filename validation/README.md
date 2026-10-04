# Validation

One script per validation case. Each script reproduces a figure (saved to
`docs/figures/`) and prints the compared quantities with their error, so
every number quoted in the README or report can be regenerated.

Planned cases (v1):

- ISA atmosphere vs. tabulated values
- Vacuum, drag-free flight vs. the Tsiolkovsky rocket equation
- Drag-free ballistic arc vs. the analytical solution
- Terminal velocity with drag vs. the analytical value
- Solid motor vs. a published commercial motor curve
- Full flight vs. OpenRocket for the same rocket and motor
