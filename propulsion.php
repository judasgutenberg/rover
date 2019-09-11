
<?php 
//boat propulsion backend. this responds to buttons in the UI for the control of the boat's overall movements
//gus mueller, august 23 2019
//////////////////////////////////////////////////////////////
 
 
//ini_set('display_errors', 1);
//ini_set('display_startup_errors', 1);
//error_reporting(E_ALL);


$command = "kill";


if($_REQUEST && $_REQUEST["command"]) {
	$command = $_REQUEST["command"];


 
	if($command=="kill") {
		$linuxCommand = escapeshellcmd('sudo python botkill.py');
		passthru($linuxCommand);
		echo '{"message":"bot killed"}';
		exit;
	} else if($command=="left") { 
		$linuxCommand = escapeshellcmd('sudo python botleft.py');
		passthru($linuxCommand);
		echo '{"message":"bot turned left"}';
		exit;
	} else if($command=="right") { 
		$linuxCommand = escapeshellcmd('sudo python botright.py');
		passthru($linuxCommand);
		echo '{"message":"bot turned right"}';
		exit;
	} else if($command=="go") { 
		$linuxCommand = escapeshellcmd('sudo python botpow.py');
		passthru($linuxCommand);
		echo '{"message":"bot going"}';
		exit;
	} else if($command=="gofast") { 
		$linuxCommand = escapeshellcmd('sudo python botpowfast.py');
		passthru($linuxCommand);
		echo '{"message":"bot going"}';
		exit;
	} else if($command=="gofastest") { 
		$linuxCommand = escapeshellcmd('sudo python botpowfastest.py');
		passthru($linuxCommand);
		echo '{"message":"bot going"}';
		exit;
	} else if($command=="rev") { 
		$linuxCommand = escapeshellcmd('sudo python botrev.py');
		passthru($linuxCommand);
		echo '{"message":"bot backing up"}';
		exit;
	}
}
