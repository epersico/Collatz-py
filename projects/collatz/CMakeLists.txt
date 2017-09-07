cmake_minimum_required (VERSION 3.8.2)

project (Collatz NONE)

message (${CMAKE_SOURCE_DIR})

find_program (COVERAGE coverage)
message      (${COVERAGE})

find_program (MAKE make)
message      (${MAKE})

find_program (MYPY mypy)
message      (${MYPY})

find_program (PYLINT pylint)
message      (${PYLINT})

find_program (PYTHON python3)
message      (${PYTHON})

add_custom_command (OUTPUT .pylintrc COMMAND ${PYLINT} --disable=locally-disabled --reports=no --generate-rcfile > .pylintrc)

add_custom_target (run)

add_custom_target (RunCollatz.pyx
    COMMAND echo -${MYPY}   ${CMAKE_SOURCE_DIR}/Collatz.py
    COMMAND      -${MYPY}   ${CMAKE_SOURCE_DIR}/Collatz.py
    COMMAND echo -${PYLINT} ${CMAKE_SOURCE_DIR}/Collatz.py
    COMMAND      -${PYLINT} ${CMAKE_SOURCE_DIR}/Collatz.py
    COMMAND echo -${MYPY}   ${CMAKE_SOURCE_DIR}/RunCollatz.py
    COMMAND      -${MYPY}   ${CMAKE_SOURCE_DIR}/RunCollatz.py
    COMMAND echo -${PYLINT} ${CMAKE_SOURCE_DIR}/RunCollatz.py
    COMMAND      -${PYLINT} ${CMAKE_SOURCE_DIR}/RunCollatz.py
    COMMAND echo ${PYTHON}  ${CMAKE_SOURCE_DIR}/RunCollatz.py '<' ${CMAKE_SOURCE_DIR}/RunCollatz.in '>' RunCollatz.tmp
    COMMAND      ${PYTHON}  ${CMAKE_SOURCE_DIR}/RunCollatz.py  <  ${CMAKE_SOURCE_DIR}/RunCollatz.in  >  RunCollatz.tmp
    COMMAND echo diff RunCollatz.tmp ${CMAKE_SOURCE_DIR}/RunCollatz.out
    COMMAND      diff RunCollatz.tmp ${CMAKE_SOURCE_DIR}/RunCollatz.out
    DEPENDS .pylintrc)
add_custom_command (TARGET run
    COMMAND ${MAKE} RunCollatz.pyx)

add_custom_target (TestCollatz.pyx
    COMMAND echo -${MYPY}                 ${CMAKE_SOURCE_DIR}/TestCollatz.py
    COMMAND      -${MYPY}                 ${CMAKE_SOURCE_DIR}/TestCollatz.py
    COMMAND echo -${PYLINT}               ${CMAKE_SOURCE_DIR}/TestCollatz.py
    COMMAND      -${PYLINT}               ${CMAKE_SOURCE_DIR}/TestCollatz.py
    COMMAND echo ${COVERAGE} run --branch ${CMAKE_SOURCE_DIR}/TestCollatz.py
    COMMAND      ${COVERAGE} run --branch ${CMAKE_SOURCE_DIR}/TestCollatz.py
    COMMAND echo ${COVERAGE} report -m
    COMMAND      ${COVERAGE} report -m
    DEPENDS .pylintrc)
add_custom_command (TARGET run
    COMMAND ${MAKE} TestCollatz.pyx)

set_property (DIRECTORY APPEND PROPERTY ADDITIONAL_MAKE_CLEAN_FILES
    ".coverage"
    ".mypy_cache")
