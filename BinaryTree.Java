import java.util.*;
import java.text.SimpleDateFormat;
import java.util.Date;

class BinaryTree{
	int value;
	BinaryTree left;
	BinaryTree right;
	
	public BinaryTree(int value)
	{
		this.value=value;
		this.left=null;
		this.right=null;
	}
	
	public void addleaf(BinaryTree nod,int value)
	{
		if (nod.left==null)
		{
			BinaryTree new_nod=new BinaryTree(value);
			nod.left=new_nod;
		}
		else if (nod.right==null)
		{
			BinaryTree new_nod=new BinaryTree(value);
			nod.right=new_nod;
		}
		else
		{
			this.addleaf(nod.left,value);
		}
	}
}
