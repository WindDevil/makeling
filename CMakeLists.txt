cmake_minimum_required(VERSION 3.20)

project(
  makeling
  VERSION 0.1.0
  DESCRIPTION "Hands-on exercises for learning GNU Make"
  LANGUAGES NONE
)

# find_program rather than find_package(Python3): the latter rejects pyenv and
# asdf shims, which are ordinary working interpreters but not real paths.
find_program(MAKELING_PYTHON NAMES python3 python REQUIRED)

enable_testing()

# Every solution is registered with CTest.  A test does exactly what
# `./makeling verify <exercise>` does: stage the solution in build/makeling/
# and replay the contract from the exercise's checks.json.  There is nothing to
# compile, which is why this project declares no languages.
file(
  GLOB makeling_solutions
  RELATIVE "${CMAKE_CURRENT_SOURCE_DIR}/solutions"
  "${CMAKE_CURRENT_SOURCE_DIR}/solutions/*/*"
)
foreach(exercise IN LISTS makeling_solutions)
  string(REPLACE "/" "_" name "solution_${exercise}")
  add_test(
    NAME ${name}
    COMMAND
      "${MAKELING_PYTHON}" "${CMAKE_CURRENT_SOURCE_DIR}/makeling"
      verify "${exercise}"
    WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
  )
endforeach()

add_custom_target(
  verify
  COMMAND
    "${MAKELING_PYTHON}" "${CMAKE_CURRENT_SOURCE_DIR}/makeling" verify
  WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
  COMMENT "Running every solution against its checks"
)

add_custom_target(
  selftest
  COMMAND
    "${MAKELING_PYTHON}" "${CMAKE_CURRENT_SOURCE_DIR}/makeling" selftest
  WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
  COMMENT "Checking that exercises start unsolved and solutions pass"
)

add_custom_target(
  generate
  COMMAND
    "${MAKELING_PYTHON}"
    "${CMAKE_CURRENT_SOURCE_DIR}/tools/generate_exercises.py"
  WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
  COMMENT "Regenerating exercises from tools/specs_*.py"
)

add_custom_target(
  check-generated
  COMMAND
    "${MAKELING_PYTHON}"
    "${CMAKE_CURRENT_SOURCE_DIR}/tools/generate_exercises.py" --check
  WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
  COMMENT "Checking that the generated files are up to date"
)
