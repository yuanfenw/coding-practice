<!DOCTYPE html>
<html class="firefox" xmlns="http://www.w3.org/1999/xhtml"><head>
	    <!-- Chartbeat code starts here -->
    <script type="text/javascript">var _sf_startpt=(new Date()).getTime()</script>
    <!-- Chartbeat code ends here -->
	<title>Interviewstreet - Facebook hiring sample test</title>
        <!-- base href="https://www.interviewstreet.com/recruit/" -->
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" type="text/css" href="read_stdin_files/userstyles.css">
        <link rel="stylesheet" href="read_stdin_files/theme.css" type="text/css">
        <link rel="shortcut icon" href="https://www.interviewstreet.com/favicon.ico">
        <script type="text/javascript">
            window.cdn_url = "https://d3rpyts3de3lx8.cloudfront.net/recruit/";
            window.base_url = "https://www.interviewstreet.com/recruit/";
        </script>
            </head>
    <body class="noI" id="public">
      <!--[if lt IE 7]>
      <div style='border: 1px solid #F7941D; background: #FEEFDA; text-align: center; clear: both; height: 75px; position: relative;'>
        <div style='position: absolute; right: 3px; top: 3px; font-family: courier new; font-weight: bold;'><a href='#' onclick='javascript:this.parentNode.parentNode.style.display="none"; return false;'><img src='http://www.ie6nomore.com/files/theme/ie6nomore-cornerx.jpg' style='border: none;' alt='Close this notice'/></a></div>
        <div style='width: 640px; margin: 0 auto; text-align: left; padding: 0; overflow: hidden; color: black;'>
          <div style='width: 75px; float: left;'><img src='http://www.ie6nomore.com/files/theme/ie6nomore-warning.jpg' alt='Warning!'/></div>
          <div style='width: 275px; float: left; font-family: Arial, sans-serif;'>
            <div style='font-size: 14px; font-weight: bold; margin-top: 12px;'>You are using an outdated browser</div>
            <div style='font-size: 12px; margin-top: 6px; line-height: 12px;'>For a better experience using this site, please upgrade to a modern web browser.</div>
          </div>
          <div style='width: 75px; float: left;'><a href='http://www.firefox.com' target='_blank'><img src='http://www.ie6nomore.com/files/theme/ie6nomore-firefox.jpg' style='border: none;' alt='Get Firefox 3.5'/></a></div>
          <div style='width: 75px; float: left;'><a href='http://www.browserforthebetter.com/download.html' target='_blank'><img src='http://www.ie6nomore.com/files/theme/ie6nomore-ie8.jpg' style='border: none;' alt='Get Internet Explorer 8'/></a></div>
          <div style='width: 73px; float: left;'><a href='http://www.apple.com/safari/download/' target='_blank'><img src='http://www.ie6nomore.com/files/theme/ie6nomore-safari.jpg' style='border: none;' alt='Get Safari 4'/></a></div>
          <div style='float: left;'><a href='http://www.google.com/chrome' target='_blank'><img src='http://www.ie6nomore.com/files/theme/ie6nomore-chrome.jpg' style='border: none;' alt='Get Google Chrome'/></a></div>
        </div>
      </div>
      <![endif]-->
        
        <div id="container" class="container">
            <h1>
                <img src="read_stdin_files/facebook-logo.jpg" alt="">
            </h1>
                <div class="right" style="padding-bottom:10px;">[ yuanfengwang@gmail.com ]</div>

       

            <div id="content" class="container">
                <div class="info span-24">
                    <div class="span-17">
                        <h2>Facebook hiring sample test</h2>
                    </div>
                    <div class="span-7 last m" style="padding:0px;">
                        <a href="https://www.interviewstreet.com/recruit/test/view/4e14032d4e529/?hash=9bf31c7ff062936a96d3c8bd1f8f2ff3">Back to Question List</a>
                        <div style="background: none repeat scroll 0% 0% rgb(142, 40, 0);" class="hasCountdown" id="timer">Time Remaining:  00:03:27</div>
                    </div>
                </div> <!-- #info -->
            </div> <!-- #content -->

            <div class="container">
            <form action="https://www.interviewstreet.com/recruit/test/view/4e14032d4e529/4ced5a1709fb1" method="post" accept-charset="utf-8" id="testquestion" class="wufoo" enctype="multipart/form-data">            <input id="tid" name="tid" value="4e14032d4e529" type="hidden">
            <input id="qid" name="qid" value="4ced5a1709fb1" type="hidden">
            <input id="autosave" name="autosave" value="" type="hidden">
				<ul>
					<li class="section first">
                        <div class="m"><strong>Question 1 / 1</strong></div>
                        <div class="question"><p><br>There are <strong>K</strong> pegs. Each peg can hold discs in decreasing order of radius when looked from bottom to top of the peg. There are <strong>N</strong> discs which have radius 1 to <strong>N</strong>;
 Given the initial configuration of the pegs and the final configuration
 of the pegs, output the moves required to transform from the initial to
 final configuration. You are required to do the transformations in 
minimal number of moves.</p>
<ul>
<li>A move consists of picking the topmost disc of any one of the pegs and placing it on top of anyother peg.</li>
<li>At anypoint of time, the decreasing radius property of all the pegs must be maintained.</li>
</ul>
<p><br> Constraints:<br> 1&lt;= <strong>N</strong>&lt;=8<br> 3&lt;= <strong>K</strong>&lt;=5<br> <br> <br> Input Format:<br> <strong>N</strong> <strong>K</strong><br> 2nd line contains <strong>N</strong> integers.<br>Each integer in the second line is in the range 1 to <strong>K </strong>where&nbsp;the <strong>i</strong>-th integer denotes the peg to which disc of radius <strong>i</strong> is present in the initial configuration.<br>3rd line denotes the final configuration in a format similar to the initial configuration.</p>
<p><br> Output Format:<br> The first line contains <strong>M</strong> - The minimal number of moves required to complete the transformation. <br> The following <strong>M</strong> lines describe a move, by a peg number to pick from and a peg number to place on.<br>
 If there are more than one solutions, it's sufficient to output any one
 of them. You can assume, there is always a solution with less than 7 
moves and the initial confirguration will not be same as the final one.<br> <br>Sample Input #00:</p>
<pre> 
2 3
1 1
2 2
</pre>
<p>Sample Output #00:</p>
<pre> 
3
1 3
1 2
3 2
</pre>
<p><br> <br> Sample Input #01:</p>
<pre>6 4
4 2 4 3 1 1
1 1 1 1 1 1
</pre>
<p>Sample Output #01:</p>
<pre>5
3 1
4 3
4 1
2 1
3 1
</pre>
<p>NOTE: You need to write the full code taking all inputs are from <strong>stdin</strong> and outputs to <strong>stdout</strong> <br> If you are using "Java", the classname is "<strong>Solution</strong>"</p></div>
					</li>


<div id="download-test-cases" style="margin-bottom:20px;">
<img src="read_stdin_files/download.png">&nbsp;&nbsp;<a target="_blank" href="https://www.interviewstreet.com/recruit/test/downloadsamplecase/4ced5a1709fb1/">Download sample testcases as zip</a> <small> ['Compile &amp; Test' will run your code against these testcases] </small> </div>
<input id="frames_json" name="frames_json" type="hidden">

<style type="text/css">
/* IE7 fix for tiny fonts - caused by clash with Wufoo. Sigh */
    div {
        font-size: 1em !important;
    }
</style>
<div id="codeshell">
<div id="codeAreaMarkup">            <div id="language-switcher">                            <span style="margin-right: 10px"> Pick your language </span>                                        <a href="#" onclick="return false;" class="language-tab" data-lang="c"> C </a>                            <a href="#" onclick="return false;" class="language-tab" data-lang="cpp"> C++ </a>                            <a href="#" onclick="return false;" class="language-tab" data-lang="java"> Java </a>                            <a href="#" onclick="return false;" class="language-tab" data-lang="csharp"> C# </a>                            <a href="#" onclick="return false;" class="language-tab" data-lang="php"> PHP </a>                            <a href="#" onclick="return false;" class="language-tab" data-lang="ruby"> Ruby </a>                            <a href="#" onclick="return false;" class="language-tab active power" data-lang="python"> Python </a>                            <a href="#" onclick="return false;" class="language-tab" data-lang="perl"> Perl </a>                    </div>            <textarea style="display: none;" id="codeArea" name="answer">#Write your code here

import sys
data = sys.stdin.readlines()
print "Counted", len(data), "lines."
print int(data[1].split())</textarea><div class="CodeMirror CodeMirror-focused"><div style="overflow: hidden; position: relative; width: 1px; height: 0px; top: 80px;"><textarea style="position: absolute; width: 2px;" wrap="off">print "Counted", len(data), "lines."
print int(data[1].split())</textarea></div><div class="CodeMirror-scroll cm-s-default"><div style="position: relative; height: 108px;"><div style="position: absolute; height: 0; width: 0; overflow: hidden;"><pre><span><span class="cm-keyword">print</span><span class="cm-null"> </span></span></pre></div><div style="position: relative; top: 0px;"><div style="height: 500px;" class="CodeMirror-gutter"><div class="CodeMirror-gutter-text"><pre>1</pre><pre>2</pre><pre>3</pre><pre>4</pre><pre>5</pre><pre>6</pre></div></div><div class="CodeMirror-lines"><div style="position: relative; margin-left: 33px;"><pre style="top: 80px; left: 60px;" class="CodeMirror-cursor">&nbsp;</pre><div style=""><pre><span class="cm-comment">#Write your code here</span></pre><pre> </pre><pre><span class="cm-keyword">import</span><span class="cm-null"> </span><span class="cm-variable">sys</span></pre><pre><span class="cm-variable">data</span><span class="cm-null"> = </span><span class="cm-variable">sys.stdin.readlines</span><span class="cm-null">()</span></pre><pre class=""><span class="cm-keyword">print</span><span class="cm-null"> </span><span class="cm-string">"Counted"</span><span class="cm-null">, </span><span class="cm-variable">len</span><span class="cm-null">(</span><span class="cm-variable">data</span><span class="cm-null">), </span><span class="cm-string">"lines."</span></pre><pre class="activeline"><span class="cm-keyword">print</span><span class="cm-null"> </span><span class="cm-builtin">int</span><span class="cm-null">(</span><span class="cm-variable">data</span><span class="cm-null">[</span><span class="cm-number">1</span><span class="cm-null">]</span><span class="cm-variable">.split</span><span class="cm-null">())</span></pre></div></div></div></div></div></div></div>            <input value="python" id="langInput" name="lang" type="hidden">            <div id="keyboard-shortcuts" style="cursor: pointer">                                <img src="read_stdin_files/keyboard.png"> Keyboard Shortcuts Available                    <span id="shortcuts-list" style="display:none; color: #888">                                            Alt-C - <strong>Compile</strong>                                        Ctrl-Space - <strong>Autocomplete</strong>. Ctrl-Z - <strong>Undo</strong>. Ctrl-R - <strong>Redo</strong></span>                    </div>        </div></div>
<script type="text/javascript">
var codeStorage = {"c":{"code":"\/*\nPlease write complete compilable code.\nRead input from standard input (STDIN) and print output to standard output(STDOUT).\nFor more details, please check https:\/\/www.interviewstreet.com\/recruit\/challenges\/faq\/view#stdio\n*\/","startLine":1},"cpp":{"code":"\/*\nPlease write complete compilable code.\nRead input from standard input (STDIN) and print output to standard output(STDOUT).\nFor more details, please check https:\/\/www.interviewstreet.com\/recruit\/challenges\/faq\/view#stdio\n*\/","startLine":1},"java":{"code":"\/*\nPlease write complete compilable code.\nYour class should be named Solution\nRead input from standard input (STDIN) and print output to standard output(STDOUT).\nFor more details, please check https:\/\/www.interviewstreet.com\/recruit\/challenges\/faq\/view#stdio\n*\/","startLine":1},"csharp":{"code":"\/*\nPlease write complete compilable code.\nRead input from standard input (STDIN) and print output to standard output(STDOUT).\nFor more details, please check https:\/\/www.interviewstreet.com\/recruit\/challenges\/faq\/view#stdio\n*\/","startLine":1},"php":{"code":"\/* Write your PHP code here *\/","startLine":1},"ruby":{"code":"=Write your code here","startLine":1},"python":{"code":"#Write your code here","startLine":1},"perl":{"code":"#Write your perl code here","startLine":1}};
</script>

<li class="buttons">

<button name="compileandTest" type="button" id="compileandTest" class="submit long">Compile &amp; Test</button><input name="" value="Submit Answer" id="saveForm" class="submit long" type="submit"><button name="" type="button" id="move-nextQuestion" class="right submit long">Skip Question</button>
</li> <!-- .buttons -->

				</ul>
            </form>            </div>
			<div id="compileandTestOuput" style="padding-left:20px;"></div>
<div class="container">
    <div id="footer" class="m span-24">
    <div style="padding: 10px 0px"> <center><small> <i> &nbsp; &nbsp; Powered by </i> </small></center></div> <a href="http://www.interviewstreet.com/" target="_blank"><img src="read_stdin_files/logo.png" alt="Interviewstreet" title="Interviewstreet" width="80" border="0" height="28"></a></div>
</div>
        </div>  <!-- #container -->
        <!-- Chartbeat code starts here -->
        <script type="text/javascript">
            var _sf_async_config={uid:34206,domain:"recruit.interviewstreet.com"};
            (function(){
              function loadChartbeat() {
                window._sf_endpt=(new Date()).getTime();
                var e = document.createElement('script');
                e.setAttribute('language', 'javascript');
                e.setAttribute('type', 'text/javascript');
                e.setAttribute('src',
                   (("https:" == document.location.protocol) ? "https://a248.e.akamai.net/chartbeat.download.akamai.com/102508/" : "http://static.chartbeat.com/") +
                   "js/chartbeat.js");
                document.body.appendChild(e);
              }
              var oldonload = window.onload;
              window.onload = (typeof window.onload != 'function') ?
                 loadChartbeat : function() { oldonload(); loadChartbeat(); };
            })();
        </script>
        <!-- Chartbeat code ends here -->
    
<script type="text/javascript" src="read_stdin_files/jquery.js"></script>
<script type="text/javascript" src="read_stdin_files/userscripts.js"></script>
<script type="text/javascript" src="read_stdin_files/codeshellscripts.js"></script>
<link rel="stylesheet" type="text/css" href="read_stdin_files/codeshellstyles.css">
<!-- <script type="text/javascript" src="https://use.typekit.com/afp2pqr.js"></script> -->
<script type="text/javascript">try{Typekit.load();}catch(e){}</script>
<textarea id="lastAttemptCode" style="display: none;"></textarea>


<script type="text/javascript">

function gotoFullScreen() {
var el = document.documentElement, rfs = 
           el.requestFullScreen
        || el.webkitRequestFullScreen
        || el.mozRequestFullScreen
        || el.msRequestFullScreen
;
if(typeof rfs!="undefined" && rfs) {
  rfs.call(el);
} else if(typeof window.ActiveXObject!="undefined") {
  // for Internet Explorer
  var wscript = new ActiveXObject("WScript.Shell");
  if (wscript!=null) {
     wscript.SendKeys("{F11}");
  }
}
}

$(document).ready(function() {
     var startIdleTime = null;
     var lastIdleTime = null;
     var lastIdleDate = null;
     var timeDiff = null;
     var totalIdleTime = null;
     var idleTimeout = 15 * 1000;
     $.idleTimer(idleTimeout);
     $(document).bind('idle.idleTimer', function() {
         lastIdleDate = new Date();
         lastIdleTime = Date.UTC(lastIdleDate.getFullYear(), lastIdleDate.getMonth(), lastIdleDate.getDate(), lastIdleDate.getHours(), lastIdleDate.getMinutes(), lastIdleDate.getSeconds(), lastIdleDate.getMilliseconds()) - idleTimeout;
         //lastIdleTime = (new Date()).getTime() - idleTimeout;
         startIdleTime = lastIdleTime;
     });
 
     $(document).bind('active.idleTimer', function() {
         var curDate = new Date();
         var curTime = Date.UTC(curDate.getFullYear(), curDate.getMonth(), curDate.getDate(), curDate.getHours(), curDate.getMinutes(), curDate.getSeconds(), curDate.getMilliseconds());
         timeDiff = curTime - lastIdleTime;
         pingServer();
         lastIdleTime = null;
         startIdleTime = null;
     });

     function pingServer(){
         if(lastIdleTime) {
             var curDate = new Date();
             var curTime = Date.UTC(curDate.getFullYear(), curDate.getMonth(), curDate.getDate(), curDate.getHours(), curDate.getMinutes(), curDate.getSeconds(), curDate.getMilliseconds());
             timeDiff = curTime - lastIdleTime;
             lastIdleTime = curTime;
         }

         totalIdleTime = curTime - startIdleTime;
              var data = {
                aid: "393293"                
         };
         if(timeDiff) {
             data.idle = timeDiff;
         }
         if(totalIdleTime) {
             data.total_idle = totalIdleTime;
         }
                  var answer = $("#codeshell").codeShell('getValue');
         var lang = $("#codeshell").codeShell('getCurrentLanguage');
         data.qid = 700;
         data.answer = answer;
         data.lang = lang;
                  $.ajax({
             data: data,
             url: window.base_url + "test/ping/4e14032d4e529/",
             type: 'POST',
             timeout: 2000
         });
              timeDiff = null;
     }

    
    
        var question_id = $("#qid").val();

        var current_user_hash = readCookie('userhash');
        var local_storage_key = current_user_hash + '-' + question_id ;
        $('#customTestCase').click(function(){
            $('#customTestInput')[0].style.display = this.checked?'block':'none';
        });


        // If the local storage has some data for this particular question, then show that.
        // Else, show server data. Server data can never be null, even for the first time.

        var local_submission_data = $.jStorage.get(local_storage_key);
        var server_submission_data = {
            language : "",
            answer : $("#lastAttemptCode").val()
        };

        var display_language = null;
        if(local_submission_data !== null && local_submission_data.language !== null && local_submission_data.language != '' ){
            codeStorage[local_submission_data.language]['code']  = local_submission_data.answer;
            display_language = local_submission_data.language;
        }
        else if(server_submission_data !== null && server_submission_data.language !== null && server_submission_data.language != ''){
            codeStorage[server_submission_data.language]['code'] = server_submission_data.answer;
            display_language = server_submission_data.language;
        }
    
        // Now initialize the code editor
        $("#codeshell").codeShell({
            currentLanguage: display_language,
            codeStorage: codeStorage,
            onCompile: function(editor) {
                $("#compileandTest").click();
            },
            keyboardImage: "https://d3rpyts3de3lx8.cloudfront.net/recruit/images/keyboard.png"
        });

        // Save the user's code every 60 seconds
        $.doTimeout( 60000, function(){
            var current_question_data = {
                answer: $("#codeshell").codeShell('getValue'),
                language: $("#codeshell").codeShell('getCurrentLanguage')
            }
            $.jStorage.set(local_storage_key, current_question_data); 
            return true;
        });
        $(".tooltip").qtip({
            position: {
                my: "top center",
                at: "bottom center"
            },
            style: {
                classes: 'ui-tooltip-shadow ui-tooltip-rounded'
            }
        });

        $('#saveForm').click(function(){
            var answer = $("#codeshell").codeShell('getValue');
            var lang = $("#codeshell").codeShell('getCurrentLanguage');

            // Save it to local storage first
            var current_question = {
                answer: answer,
                language: lang
            };
            $.jStorage.set(local_storage_key, current_question)
            return true;
        });

        $("#compileandTest").click(function() {

            // Disable compile and test for two seconds
            $("#compileandTest").attr("disabled", true);
            $.doTimeout(2000, function(){
                $("#compileandTest").attr('disabled', false);
                return false;
            });

            // Show a loading button
            // TODO: this is ugly way of doing it. Show it in a nice way
            $("#compileandTestOuput").html("<img src='https://d3rpyts3de3lx8.cloudfront.net/recruit/images/running.gif' alt='' align='left'> &nbsp;&nbsp;&nbsp;Compiling and running your code. Please wait...");

            // Get the latest code and language from editor
            var answer = $("#codeshell").codeShell('getValue');
            var lang = $("#codeshell").codeShell('getCurrentLanguage');

            // Save it to local storage first
            var current_question = {
                answer: answer,
                language: lang
            };
            $.jStorage.set(local_storage_key, current_question)

            // Submit to server and show compile and test output
            $.post("test/compiletest/", 
            {
                "qid": question_id,
                "answer": answer, 
                "lang": lang ,
                "sample": true,
                "test_hash" : "4e14032d4e529",
                            }, function(data) {
                $("#compileandTestOuput").html(data);
                $('html, body').animate({ scrollTop: $('#compileandTestOuput').offset().top }, 'fast');
                $('.view-diff-link').click(function(){
                    $(this).parent().next().slideToggle();
                    return false;
                });
            });

            return false;
        });

        $(".compileandTestAll").live('click', function() {
            // Disable compile and test for two seconds
            $("#compileandTest").attr("disabled", true);
            $.doTimeout(2000, function(){
                $("#compileandTest").attr('disabled', false);
                return false;
            });

            // Disable compile and test for two seconds
            $(".compileandTestAll").attr("disabled", true);
            $.doTimeout(2000, function(){
                $(".compileandTestAll").attr('disabled', false);
                return false;
            });

            // Show a loading button
            // TODO: this is ugly way of doing it. Show it in a nice way
            $("#compileandTestOuput").html("<img src='https://d3rpyts3de3lx8.cloudfront.net/recruit/images/running.gif' alt='' align='left'> &nbsp;&nbsp;&nbsp;Compiling and running your code. Please wait...");

            // Get the latest code and language from editor
            var answer = $("#codeshell").codeShell('getValue');
            var lang = $("#codeshell").codeShell('getCurrentLanguage');

            // Save it to local storage first
            var current_question = {
                answer: answer,
                language: lang
            };
            $.jStorage.set(local_storage_key, current_question)

            // Submit to server and show compile and test output
            $.post("test/compiletest/", 
            {
                "qid": question_id,
                "answer": answer, 
                "lang": lang ,
                "sample": false,
                "test_hash" : "4e14032d4e529",
                            }, function(data) {
                $("#compileandTestOuput").html(data);
                $('html, body').animate({ scrollTop: $('#compileandTestOuput').offset().top }, 'fast');
                $('.view-diff-link').click(function(){
                    $(this).parent().next().slideToggle();
                    return false;
                });
            });

            return false;
        });

        // Handle recording.
                

                        $(document).ready(function() {
                function showTimerWarning(ticks) {
                    var timeRemaining = $.countdown.periodsToSeconds(ticks);
                    if (timeRemaining == 120) { $.notifyBar({  cls: "error", html: "This test will end in 2 minutes. Please click on 'Submit answer' for your answer to be evaluated.", delay: 5000, animationSpeed: "normal" }); }
                    if (timeRemaining == 300) { $.notifyBar({  cls: "error", html: "This test will end in 5 minutes. Please click on 'Submit answer' for your answer to be evaluated.", delay: 5000, animationSpeed: "normal" }); }
                    if (timeRemaining < 300) { $("#timer").css('background', '#8e2800'); }
                    if (timeRemaining < 5) { testDone = true; }

                                        if (timeRemaining % 60 == 0) {
                       pingServer();
                    }
                                    }

                function showSectionTimerWarning(ticks) {
                    var timeRemaining = $.countdown.periodsToSeconds(ticks);
                    if (timeRemaining == 120) { $.notifyBar({  cls: "error", html: "This section will end in 2 minutes. Please click on 'Submit answer' for your answer to be evaluated.", delay: 5000, animationSpeed: "normal" }); }
                    if (timeRemaining == 300) { $.notifyBar({  cls: "error", html: "This section will end in 5 minutes. Please click on 'Submit answer' for your answer to be evaluated.", delay: 5000, animationSpeed: "normal" }); }
                    if (timeRemaining < 300) { $("#timer").css('background', '#8e2800'); }
                    if (timeRemaining < 5) { testSectionDone = true; }

                                        if (timeRemaining % 60 == 0) {
                       pingServer();
                    }
                                    }

                var d = new Date();
                d.setTime(d.getTime() + 2764000);
                                $('#timer').countdown({until: d, layout: 'Time Remaining: {d<}{dn}{dl} {d>} {hnn}:{mnn}:{snn}', expiryUrl: 'test/view/4e14032d4e529/done/', onTick: showTimerWarning, compact: true});
                            });
            });

    if(self!=parent) {
        window.onload = init;
        $(this).bind( "ajaxComplete", init);
    }

    function init() {
        $.postMessage({ if_height: $('body').outerHeight( true )}, '' );
    }

</script>

<!-- Enable Copy/Paste Contextmenu protection -->

<script type="text/javascript">
 
/*    mpq.name_tag('yuanfengwang@gmail.com'); 
    mpq.track('Page Load Time', {'CI Benchmark Time' : 0.1611, 'Test ID' : '4e14032d4e529',  'Question ID' : '4ced5a1709fb1'});
    window.onerror = function(message, url, linenumber) {
        mpq.track("Javascript error", { 'message': message, 'url': url, 'linenumber': linenumber});
    }*/
</script>


<script>
    var submitClicked = false;
    var textareaChanged = false;
    var globalFirstLoad = true;
    var testDone = false;
	
    $(document).ready(function() {

        $("#move-prevQuestion").click(function() { window.location = "https://www.interviewstreet.com/recruit/test/view/4e14032d4e529//?randhash=375457"; });

        prettyPrint();

        $("#saveForm").click(function() {
            submitClicked = true;
                        // Save the language the user used to code as a cookie, so that it can be reused
            var current_language = $(".currentlanguageblock a").attr('id');
            $.cookie("user_language", current_language, { path: "/" });
                    });
        $("#textarea_2").bind("change", function() { textareaChanged = true; });

    });

    $(window).bind('beforeunload', function() {
        if (submitClicked == true || testDone == true) { return; }
            if (textareaChanged == true) {
                return "You haven't saved your answer. If you navigate away from this page, you might LOSE your changes.";
            }
        var dirtyLanguages = $("#codeshell").codeShell("getDirtyLanguages");
        if (dirtyLanguages.length > 0) {
            var langText = "";
            $.each(dirtyLanguages, function(i, lang) {
                if(i == dirtyLanguages.length - 1) { // Last Element
                    langText += lang;
                } else if (i == dirtyLanguages.length - 2) {
                    langText += lang + " and ";
                } else {
                    langText += lang + ", ";
                }
            }); 
            var langWarning = "You have unsaved " + langText + " code.\nPlease submit your code before leaving the page";
            return langWarning;
        }
    });


    (function(){
      /* Toggle the panel show & hide*/
      var togglePanel = function(){
        if ($('#progressbar-panel').hasClass('collapse'))
        {
          $('#progressbar-panel').addClass('expand');
          $('#progressbar-panel').removeClass('collapse');
          $('#progressbar-panel .progress').animate({'left':'-3px'}, 500);
          $.cookie('progresspanel-pref', 'expand', { path: "/"});
        }
        else
        {
          $('#progressbar-panel .progress').animate({'left':'-150px'}, 500, function(){
            $('#progressbar-panel').addClass('collapse');
            $('#progressbar-panel').removeClass('expand');
            $.cookie('progresspanel-pref', 'collapse', { path: "/"} );
          });
        }
        return false;
      }

      /* Listeners */
      $('.trigger').click(togglePanel);
      $('#progress-close').click(togglePanel);
    })();


</script>
<!-- 10.100.6.65 -->
<script src="read_stdin_files/chartbeat.js" type="text/javascript" language="javascript"></script></body></html>