def annotate_graph(chemical_symbol, crystal_symmetry):
    import matplotlib.pyplot as plt
    Au = plt.text(130, -0.038, chemical_symbol, horizontalalignment='left', verticalalignment='top')
    ggA_PBEsol = plt.text(130, -0.02, crystal_symmetry, horizontalalignment='center', verticalalignment='center')

    return Au, ggA_PBEsol


