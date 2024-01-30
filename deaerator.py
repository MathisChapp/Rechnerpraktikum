from tespy.networks import Network
from tespy.components import (Sink, Source, Merge)
from tespy.connections import Connection

# fluids
water = {'H2O': 1}

# network
deaerator = Network(T_unit='C', p_unit='bar', h_unit='kJ / kg', m_unit='kg / s')

# components
src_water = Source('water-source')
src_steam = Source('steam-source')
snk_feedwater = Sink('feedwater-sink')
cmp_mrg = Merge('merge')

# connection
c01 = Connection(src_water, 'out1', cmp_mrg, 'in1')
c02 = Connection(src_steam, 'out1', cmp_mrg, 'in2')
c03 = Connection(cmp_mrg, 'out1', snk_feedwater, 'in1')

deaerator.add_conns(c01, c02, c03)

# parameters

# components

# connections
c01.set_attr(m=1, p=4, T=60, fluid=water)
c02.set_attr(x=1, fluid=water)
c03.set_attr(x=0)

# solve
deaerator.solve(mode='design')
deaerator.print_results()