import matplotlib.pyplot as plt

list1 = [1, 2, 3, 4, 5, 6, 2, 4, 5, 9]
list2 = [1, 2, 3, 5, 6, 7, 2, 4, 5, 9]
list3 = [1, 2, 3, 4, 5, 6, 2, 5, 9]

# plt.boxplot(list1)
# plt.boxplot(list2)
# plt.boxplot(list3)

# put the lists into a master list
data_to_plot = [list1, list2, list3]

# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data_to_plot)

## add patch_artist=True option to ax.boxplot() 
## to get fill color
bp = ax.boxplot(data_to_plot, patch_artist=True)

## change outline color, fill color and linewidth of the boxes
for box in bp['boxes']:
    # change outline color
    box.set( color='#000000', linewidth=2)
    # change fill color
    box.set( facecolor = '#ffff00' )

## change color and linewidth of the whiskers
for whisker in bp['whiskers']:
    whisker.set(color='#000000', linewidth=2)

## change color and linewidth of the caps
for cap in bp['caps']:
    cap.set(color='#000000', linewidth=2)

## change color and linewidth of the medians
for median in bp['medians']:
    median.set(color='#cc0000', linewidth=2)

## change the style of fliers and their fill
for flier in bp['fliers']:
    flier.set(marker='o', color='#ffff00', alpha=0.5)

# Save the figure
fig.savefig('fig1.png', bbox_inches='tight')

# change labels
ax.set_xticklabels(['List 1', 'List 2', 'List 3'])

plt.show()