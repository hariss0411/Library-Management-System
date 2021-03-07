<?php
	include "common.php";
	  
	
	
    //$command = escapeshellcmd("python s1.py $cat");
	//$command = passthru("python s1.py $cat");
    //$output = shell_exec($command);
	if(isset($_POST['cat'])){
		$cat =$_POST['cat'];
		exec("python s1.py $cat",$output);
		session_start();
		$_SESSION['info']=$output;
		//echo $output[0];
		//echo $output[1];
	}
	if(isset($_POST['need'])){
		$need=$_POST['need'];
		$command = escapeshellcmd("python s2.py $need");
		$output = shell_exec($command);
		session_start();
		$_SESSION['info1']=$output;
	}
	
	header("location:stud_zone.php");
?>