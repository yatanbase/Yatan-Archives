package com.yatan.thisbitch

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    override fun onStart() {
        super.onStart()
        println("onstart")
    }

    override fun onResume() {
        super.onResume()
        println("onresume")
    }

    override fun onPause() {
        super.onPause()
        println("onpause")
    }

    override fun onStop() {
        super.onStop()
        println("onstop")
    }

    override fun onDestroy() {
        super.onDestroy()
        println("ondestroy")
    }
}