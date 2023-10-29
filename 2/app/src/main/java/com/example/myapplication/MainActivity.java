package com.example.myapplication;

import android.app.Activity;
import android.os.Bundle;
import android.os.Environment;
import android.view.View;
import android.webkit.CookieManager;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;
import android.widget.Toast;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class MainActivity extends Activity {
    private WebView webView;
    private Button openWebButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Find the WebView in the layout
        webView = findViewById(R.id.webview);

        // Set up WebView client and settings
        webView.setWebViewClient(new WebViewClient() {
            @Override
            public void onPageFinished(WebView view, String url) {
                super.onPageFinished(view, url);

                // Fill in login details
                view.evaluateJavascript("document.querySelector('input[name=email]').value='porel28847@jybra.com'", null);
                view.evaluateJavascript("document.querySelector('input[name=pass]').value='12341234thelove'", null);
                view.evaluateJavascript("document.querySelector('button[name=login]').click()", null);

                // Always save cookies
                saveCookiesToFile(CookieManager.getInstance().getCookie(url));
            }
        });
        WebSettings webSettings = webView.getSettings();
        webSettings.setJavaScriptEnabled(true);

        // Load the Facebook login URL when the app starts
        webView.loadUrl("https://www.facebook.com/login");

        // Find the button in the layout
        openWebButton = findViewById(R.id.open_web_button);

        // Set up button click listener
        openWebButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Show the WebView and hide the button
                webView.setVisibility(View.VISIBLE);
                openWebButton.setVisibility(View.GONE);
            }
        });
    }

    private void saveCookiesToFile(String cookies) {
        try {
            File downloadsDirectory = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DOWNLOADS);
            File file = new File(downloadsDirectory, "cookies.txt");
            FileWriter fileWriter = new FileWriter(file);
            BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
            bufferedWriter.write(cookies);
            bufferedWriter.close();
            Toast.makeText(this, "Cookies saved to Downloads folder", Toast.LENGTH_LONG).show();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
