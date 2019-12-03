def state_plotter(states):
    
    fig, ax = plt.subplots(figsize=(30,30))
    usa[1:50].plot(ax=ax,alpha = 0.3)
    
    for n in states:
        usa[usa.STATE_ABBR == f'{n}'].plot(ax=ax, edgecolor='y', linewidth =2)