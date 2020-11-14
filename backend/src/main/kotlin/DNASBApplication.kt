package com.github.grchristensen.dnasb

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class DNASBApplication

fun main(args: Array<String>) {
    runApplication<DNASBApplication>(*args)
}
