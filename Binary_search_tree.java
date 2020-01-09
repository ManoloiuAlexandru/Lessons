//https://en.wikipedia.org/wiki/Binary_search_tree
class BinaryschTree{
	int value;
	BinaryschTree left;
	BinaryschTree right;
	
	public BinaryschTree(int value)
	{
		this.value=value;
		this.left=null;
		this.right=null;
	}
	
	public BinaryschTree addleaf(BinaryschTree nod,int value)
	{
		if (nod==null)
		{
			nod=new BinaryschTree(value);
		}
		else if (value>nod.value && nod.right==null)
		{
			nod.right=new BinaryschTree(value);
		}
		else if (value<nod.value && nod.left==null)
		{
			nod.left=new BinaryschTree(value);
		}
		else if (value>nod.value && nod.right!=null)
		{
			return this.addleaf(nod.right, value);
		}
		else
		{
			return this.addleaf(nod.left, value);
		}
		return null;
	}
}
