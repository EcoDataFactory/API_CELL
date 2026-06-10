/* Copyright 2021 Braden Farmer
 *
 * Licensed under the Apache License, Version 2.0
 */

@file:OptIn(ExperimentalComposeUiApi::class)

package com.farmerbb.notepad.ui.content

import android.view.MotionEvent
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.text.selection.SelectionContainer
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.ExperimentalComposeUiApi
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Rect
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.input.pointer.pointerInteropFilter
import androidx.compose.ui.platform.LocalDensity
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.unit.dp
import com.farmerbb.notepad.ui.components.RtlTextWrapper

@Composable
fun ViewNoteContent(
    text: String,
    baseTextStyle: TextStyle = TextStyle(),
    markdown: Boolean = false,
    rtlLayout: Boolean = false,
    isPrinting: Boolean = false,
    showDoubleTapMessage: Boolean = false,
    doubleTapMessageShown: () -> Unit = {},
    onDoubleTap: (Offset?) -> Unit = {}
) {
    val textStyle = if (isPrinting) {
        baseTextStyle.copy(color = Color.Black)
    } else {
        baseTextStyle
    }

    var doubleTapTime by remember { mutableStateOf(0L) }
    var lastOffset by remember { mutableStateOf(Offset(0f, 0f)) }
    val radius = with(LocalDensity.current) { 24.dp.toPx() }

    Column(
        modifier = Modifier.fillMaxSize()
    ) {
        Box(
            modifier = if (isPrinting) {
                Modifier
            } else {
                Modifier.verticalScroll(state = rememberScrollState())
            }
        ) {
            val modifier = Modifier
                .padding(
                    horizontal = 16.dp,
                    vertical = 12.dp
                )
                .fillMaxWidth()
                .pointerInteropFilter { motionEvent ->
                    if (motionEvent.action == MotionEvent.ACTION_DOWN) {
                        val now = System.currentTimeMillis()
                        val offset = Offset(motionEvent.x, motionEvent.y)
                        val rect = Rect(center = lastOffset, radius = radius)

                        val cursorAtOffset: Offset? = if (!markdown) offset else null

                        when {
                            doubleTapTime > now && rect.contains(offset) -> onDoubleTap(cursorAtOffset)
                            showDoubleTapMessage -> doubleTapMessageShown()
                        }

                        doubleTapTime = now + 200
                        lastOffset = offset
                    }

                    false
                }

            RtlTextWrapper(text, rtlLayout) {
                SelectionContainer {
                    Text(
                        text = text,
                        style = textStyle,
                        modifier = modifier
                    )
                }
            }
        }
    }
}
