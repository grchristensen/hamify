package com.github.grchristensen.dnasb

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class DnasbApplication

fun main(args: Array<String>) {
    runApplication<DnasbApplication>(*args)
}
