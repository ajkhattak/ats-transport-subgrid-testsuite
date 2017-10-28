- solve transport on a surface mesh

dC/dt + v dC/dx = -aC + a \sum_i w_i C^sg(Tau_i)

- for some set of surface cells, hang a 1D logical? mstk? mesh off of the cell from Tau = 0 to Tau max, with variable dTau.

- solve transport (separately) on the 1D mesh in Tau, with BC given by aC at Tau=0 to calculate C^sg(Tau_i)

- check whether 1D mesh is MSTK or Logical -- can transport run in TPFA?  (yes, use logical, need to convert surface to logical too!)
- write code to create and hang 1D meshes from surface mesh (done)
- write evaluator to accumulate weighted source term \sum_i w_i C^sg above (evaluators can't work, hard coded)


Tests:

- surface-transport:  steady state flow on the surface mesh, transport using that flow
- surface-logical: steady state flow on a logical mesh, transport using that flow
- surface-logical-coplay: transport individually surface + all subgrid logicals, totally uncoupled
- surface-logical-oneway: transport on surface mesh, subgrid models take BC from surface
- surface-logical-twoway-noreturn: transport on surface mesh, subgrid models take BC from surface, surface loses C to subgrid
- surface-logical-twoway: transport on surface, subgrid models take BC from surface, surface loses C to subgrid, surface gains recharge from subgrid


Four types of DomainFunctions used:
 1. Source into surface mesh (PK_DomainFunctionVolume)
 2. BC of subgrid meshes (PK_DomainFunctionSubgrid, maps from surface C onto subgrid BCs)
 3. Sink from surface to subgrid.  (PK_DomainFunctionExponentialDecay, -alpha A C)
 4. Source to surface from subgrid. (PK_DomainFunctionSubgridReturn, alpha A sum_i w_i C_i)

Note that all things that need A should use Volume multiple on surfafce (1,3,4).

Should the BC of 2 be C_sg |_0 = alpha C_surf as suggested above?  Or C_sg |_0 = C_surf?  The latter is the current implementation.


