function init(){
	let button = document.getElementById('button');
	button.addEventListener('click', generateMsg);
}



function generateMsg(){
	let whoop=[];
	const idNames = ['noun1', 'noun2', 'verb', 'adjective', 'place'];
	whoop[0]=document.getElementById('noun1').value;
	whoop[1]=document.getElementById('noun2').value;
	whoop[2]=document.getElementById('verb').value;
	whoop[3]=document.getElementById('adjective').value;
	whoop[4]=document.getElementById('place').value;
for(let i=0; i<idNames.length; i++)
{
	if (whoop[i]==''){
		whoop[i]=idNames[i];
	}

}



	/*Using a for loop, populate the values array with the values of the
	 textfields*/


	let msg = `If anybody is wondering, please know that I am <strong>${whoop[2]}</strong> at <strong>${whoop[4]}</strong> without you.
	You might want to consider <strong>${whoop[3]}</strong> <strong>${whoop[0]}</strong>... then again, you always preferred
	<strong>${whoop[1]}</strong>.`;

	//Display the msg string in the paragraph element with id 'msg'
	document.getElementById('msg').innerHTML=msg;
}
