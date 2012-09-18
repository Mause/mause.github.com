<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Loading Demo - CSSJockey.com</title>

<!-- Code within Head Tag -->
<script type="text/javascript" src="jquery.js"></script>
<script type="text/javascript">
	$(window).load(function(){
		$("#loading").hide();		
	})
</script>
<!-- Code within Head Tag -->

<style type="text/css">
/* Document Styles */
body{
	background:#efefef;
	font:normal 9pt arial;
}
#wrapper{
	width:800px;
	height:500px;
	margin:0 auto;
	padding:5px;
	border:1px solid #CCC;
	background:#CCC;
}
.desc{
	margin:0 auto;
	width:800px;
	text-align:center;
}

/* Loadign Div Style */
#loading{
	position:absolute;
	width:300px;
	top:0px;
	left:50%;
	margin-left:-150px;
	text-align:center;
	padding:7px 0 0 0;
	font:bold 11px Arial, Helvetica, sans-serif;
}
</style>

</head>
<body>
<!-- Loading Div -->
<div id="loading">
	Loading content, please wait..
	<img src="loading.gif" alt="loading.." />
</div>
<!-- Loading Div -->

<!-- Other body elements -->
<br /><br /><br />
<div id="wrapper">
	<img src="http://www.cssjockey.com/files/downloads/wallpapers/firefox/Firefox-1920x1200.jpg" width="800" height="500" alt="Loading Demo" />
</div>
<div class="desc">
	<a href="http://www.cssjockey.com/web-design-tutorials/an-easy-way-to-create-loading-bar" title="View Tutorial">View Tutorial</a>
</div>
<!-- Other body elements -->
</body>
</html>
