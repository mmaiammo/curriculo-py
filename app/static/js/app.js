if (document.readyState) {
  document.onreadystatechange = checkstate;
} else if (document.addEventListener) {
  document.addEventListener("DOMContentLoaded", saydone, false);
}
function checkstate() {
  if (document.readyState == "complete" || document.readyState == "complete") {
    document.getElementsByClassName("main")[0].style.visibility = "visible";
  }
}

function saydone() {
  document.getElementsByClassName("main")[0].style.visibility = "visible";
}

$(function () {
  $(document).on("scroll", function () {
    if ($(window).scrollTop() > 100) {
      $(".smoothscroll-top").addClass("show");
    } else {
      $(".smoothscroll-top").removeClass("show");
    }
  });
  $(".smoothscroll-top").on("click", scrollToTop);
});

function scrollToTop() {
  verticalOffset = typeof verticalOffset != "undefined" ? verticalOffset : 0;
  element = $("body");
  offset = element.offset();
  offsetTop = offset.top;
  $("html, body")
    .animate({ scrollTop: offsetTop }, 600, "linear")
    .animate({ scrollTop: 25 }, 200)
    .animate({ scrollTop: 0 }, 150)
    .animate({ scrollTop: 0 }, 50);
}

// Troca estilo
window.onload = function () {
  var pathname = $(location).attr("pathname");
  let theme = sessionStorage.getItem("theme");

  if (theme === null) {
    if (pathname == "/") {
      document
        .getElementById("cssid")
        .setAttribute("href", "static/css/classico.min.css");
    }
  }

  if (theme !== null) {
    let cssfile = sessionStorage.getItem("theme");
    if (pathname == "/") {
      document.getElementById("cssid").setAttribute("href", cssfile);
    }
  }
};

function troca_css(cssFile) {
  var pathname = $(location).attr("pathname");
  sessionStorage.setItem("theme", cssFile);

  if (pathname == "/") {
    document.getElementById("cssid").setAttribute("href", cssFile);
  }
  if (pathname != "/") {
    window.location.href = "/";
  }
}

function print() {
  $("#a4").print({
    globalStyles: true,
    mediaPrint: false,
    stylesheet: "../static/css/print.min.css",
    noPrintSelector: ".no-print",
    iframe: true,
    append: null,
    prepend: null,
    manuallyCopyFormValues: true,
    deferred: $.Deferred(),
    timeout: 750,
    title: null,
    doctype: "<!doctype html>",
  });
}

$(document).on("scroll", function () {
  if ($(window).scrollTop() > 100) {
    $(".smoothscroll-top").addClass("show");
  } else {
    $(".smoothscroll-top").removeClass("show");
  }
});
$(".smoothscroll-top").on("click", scrollToTop);

function scrollToTop() {
  verticalOffset = typeof verticalOffset != "undefined" ? verticalOffset : 0;
  element = $("body");
  offset = element.offset();
  offsetTop = offset.top;
  $("html, body")
    .animate({ scrollTop: offsetTop }, 600, "linear")
    .animate({ scrollTop: 25 }, 200)
    .animate({ scrollTop: 0 }, 150)
    .animate({ scrollTop: 0 }, 50);
}
