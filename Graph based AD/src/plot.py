def plot(data, ylim=None):
    
    '''
    Args:
        data: <np.array> [length, 51]
        ylim: <list> [min, max]
    '''
    with plt.style.context('bmh'):
        font = {'color': 'darkred', 'size': 12, 'family': 'serif'}
        font_legend = {'size': 12, 'family': 'serif'}
        fig, axs = plt.subplots(25, 2, figsize=(60, 30))
        for i in tqdm.tqdm(range(50)):
            axs[i%25, int(i/25)].plot(data[:, i], label=f'{i}-th feature', color='blue')
            axs[i%25, int(i/25)].legend(loc='upper right', prop=font_legend)
            if ylim is not None:
                axs[i%25, int(i/25)].set_ylim(ylim)
            labels = axs[i%25, int(i/25)].get_xticklabels() + axs[i%25, int(i/25)].get_yticklabels()
            [label.set_fontname('serif') for label in labels]

    plt.tight_layout() 