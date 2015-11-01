<head>
    <title>iOS 8 web app · taylor.fausak.me</title>

    <!-- CONFIGURATION -->

    <!-- Allow web app to be run in full-screen mode. -->
    <meta name="apple-mobile-web-app-capable" content="yes">

    <!-- Make the app title different than the page title. -->
    <meta name="apple-mobile-web-app-title" content="iOS Web App">

    <!-- Configure the status bar. -->
    <meta name="apple-mobile-web-app-status-bar-style" content="black">

    <!-- Set the viewport. -->
    <meta name="viewport" content="initial-scale=1">

    <!-- Disable automatic phone number detection. -->
    <meta name="format-detection" content="telephone=no">

    <!-- ICONS -->

    <!-- iPad retina icon -->
    <link href="/static/images/apple-touch-icon-precomposed-152x152.png" sizes="152x152" rel="apple-touch-icon-precomposed">

    <!-- iPad retina icon (iOS < 7) -->
    <link href="/static/images/apple-touch-icon-precomposed-144x144.png" sizes="144x144" rel="apple-touch-icon-precomposed">

    <!-- iPad non-retina icon -->
    <link href="/static/images/apple-touch-icon-precomposed-76x76.png" sizes="76x76" rel="apple-touch-icon-precomposed">

    <!-- iPad non-retina icon (iOS < 7) -->
    <link href="/static/images/apple-touch-icon-precomposed-72x72.png" sizes="72x72" rel="apple-touch-icon-precomposed">

    <!-- iPhone 6 Plus icon -->
    <link href="/static/images/apple-touch-icon-precomposed-180x180.png" sizes="120x120" rel="apple-touch-icon-precomposed">

    <!-- iPhone retina icon (iOS < 7) -->
    <link href="/static/images/apple-touch-icon-precomposed-114x114.png" sizes="114x114" rel="apple-touch-icon-precomposed">

    <!-- iPhone non-retina icon (iOS < 7) -->
    <link href="/static/images/apple-touch-icon-precomposed-57x57.png" sizes="57x57" rel="apple-touch-icon-precomposed">

    <!-- STARTUP IMAGES -->

    <!-- iPad retina portrait startup image -->
    <link href="/static/images/apple-touch-startup-image-1536x2008.png" media="(device-width: 768px) and (device-height: 1024px)
                 and (-webkit-device-pixel-ratio: 2)
                 and (orientation: portrait)" rel="apple-touch-startup-image">

    <!-- iPad retina landscape startup image -->
    <link href="/static/images/apple-touch-startup-image-1496x2048.png" media="(device-width: 768px) and (device-height: 1024px)
                 and (-webkit-device-pixel-ratio: 2)
                 and (orientation: landscape)" rel="apple-touch-startup-image">

    <!-- iPad non-retina portrait startup image -->
    <link href="/static/images/apple-touch-startup-image-768x1004.png" media="(device-width: 768px) and (device-height: 1024px)
                 and (-webkit-device-pixel-ratio: 1)
                 and (orientation: portrait)" rel="apple-touch-startup-image">

    <!-- iPad non-retina landscape startup image -->
    <link href="/static/images/apple-touch-startup-image-748x1024.png" media="(device-width: 768px) and (device-height: 1024px)
                 and (-webkit-device-pixel-ratio: 1)
                 and (orientation: landscape)" rel="apple-touch-startup-image">

    <!-- iPhone 6 Plus portrait startup image -->
    <link href="/static/images/apple-touch-startup-image-1242x2148.png" media="(device-width: 414px) and (device-height: 736px)
                 and (-webkit-device-pixel-ratio: 3)
                 and (orientation: portrait)" rel="apple-touch-startup-image">

    <!-- iPhone 6 Plus landscape startup image -->
    <link href="/static/images/apple-touch-startup-image-1182x2208.png" media="(device-width: 414px) and (device-height: 736px)
                 and (-webkit-device-pixel-ratio: 3)
                 and (orientation: landscape)" rel="apple-touch-startup-image">

    <!-- iPhone 6 startup image -->
    <link href="/static/images/apple-touch-startup-image-750x1294.png" media="(device-width: 375px) and (device-height: 667px)
                 and (-webkit-device-pixel-ratio: 2)" rel="apple-touch-startup-image">

    <!-- iPhone 5 startup image -->
    <link href="/static/images/apple-touch-startup-image-640x1096.png" media="(device-width: 320px) and (device-height: 568px)
                 and (-webkit-device-pixel-ratio: 2)" rel="apple-touch-startup-image">

    <!-- iPhone < 5 retina startup image -->
    <link href="/static/images/apple-touch-startup-image-640x920.png" media="(device-width: 320px) and (device-height: 480px)
                 and (-webkit-device-pixel-ratio: 2)" rel="apple-touch-startup-image">

    <!-- iPhone < 5 non-retina startup image -->
    <link href="/static/images/apple-touch-startup-image-320x460.png" media="(device-width: 320px) and (device-height: 480px)
                 and (-webkit-device-pixel-ratio: 1)" rel="apple-touch-startup-image">

    <!-- HACKS -->

    <!-- Prevent text size change on orientation change. -->
    <style>
        html {
            -webkit-text-size-adjust: 100%;
        }
    </style>
</head>

<body>
<h1>
    <a href="http://taylor.fausak.me">taylor.fausak.me</a>
</h1>

<h2>iOS 8 web app</h2>

<p>
    This is an example web app for iOS 8. It includes icons and startup
    images for a wide variety of operating systems and devices. To see what
    it does, open this page on an iOS device and add it to your home screen.

    For more information, <a href="http://taylor.fausak.me/2015/01/27/ios-8-web-apps/">read the explanatory blog post</a>.

    If you still have questions, <a href="https://gist.github.com/tfausak/2222823">look for community help on the Gist</a>.
</p>

<pre id="source" style="max-width: 100%; overflow-x: auto;"></pre>

<script>
    (function () {
        var source = document.documentElement.innerHTML;
        var element = document.getElementById('source');
        element.innerText = source;
    }());
</script></body>
