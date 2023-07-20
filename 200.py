new_df = df.loc[df[filter_column] == input_box.value]

if(new_df[yaxis].min()>1000):
	plt.scatter(new_df[xaxis], new_df[yaxis], c =rgb, alpha=0.4, s=new_df[yaxis]/(new_df[yaxis].min()/2))
