#include <Python.h>
// #include "/usr/include/python3.5m/Python.h"
// #include "/usr/include/python3.4m/Python.h" online
#include "../src/judge.c"

char **generate_argv(PyObject *);

int generate_config(Config *, PyObject *);

PyObject *python_run(PyObject *, PyObject *);

PyObject *generate_result(Result *);

void initCodeNutJudge(void);

char **generate_argv(PyObject *py_args_obj) {
  if (!PyList_Check(py_args_obj)) {
    REPORTER("Argv type check fail");
    return NULL;
  }

  int len = (int)PyList_GET_SIZE(py_args_obj);

  char **argv = (char **)malloc(sizeof(char *) * (len + 1));

  int i;
  for (i = 0; i < len; i++) {
    argv[i] = PyUnicode_AsUTF8(PyList_GetItem(py_args_obj, i));
    // printf("argv[%d]: %s\n", i, argv[i]);
  }
  argv[len] = NULL;

  return argv;
}

int generate_config(Config *config, PyObject *py_object_config) {
  PyObject *tmp;

  if ((tmp = PyDict_GetItemString(py_object_config, "args")) == NULL) {
    REPORTER("Get args failed");
    return -1;
  }
  if ((config->args = generate_argv(tmp)) == NULL) {
    REPORTER("Get args failed");
    return -1;
  }

  if ((tmp = PyDict_GetItemString(py_object_config, "output")) == NULL) {
    REPORTER("Get output failed");
    return -1;
  }
  config->output = PyUnicode_AsUTF8(tmp);

  if ((tmp = PyDict_GetItemString(py_object_config, "language")) == NULL) {
    REPORTER("Get language failed");
    return -1;
  }
  config->language = PyUnicode_AsUTF8(tmp);
  REPORTER(config->language);

  if ((tmp = PyDict_GetItemString(py_object_config, "time_limit")) == NULL) {
    REPORTER("Get time limit failed");
    return -1;
  }
  config->time_limit = PyLong_AsLong(tmp);

  if ((tmp = PyDict_GetItemString(py_object_config, "memory_limit")) == NULL) {
    REPORTER("Get memory limit failed");
    return -1;
  }
  config->memory_limit = PyLong_AsLong(tmp);

  return 0;
}

PyObject *generate_result(Result *result) {
  PyObject *tmp;
  PyObject *py_object_result;

  py_object_result = PyDict_New();

  tmp = PyUnicode_FromString(result->status);
  if (PyDict_SetItemString(py_object_result, "status", tmp)) {
    REPORTER("Set status failed");
  }
  Py_DECREF(tmp);

  tmp = PyLong_FromLong(result->time_used);
  if (PyDict_SetItemString(py_object_result, "time_used", tmp)) {
    REPORTER("Set time used failed");
  }
  Py_DECREF(tmp);

  tmp = PyLong_FromLong(result->memory_used);
  if (PyDict_SetItemString(py_object_result, "memory_used", tmp)) {
    REPORTER("Set memory used failed");
  }
  Py_DECREF(tmp);

  return py_object_result;
}

PyObject *python_run(PyObject *self, PyObject *argv) {
  PyObject *py_object_config;
  PyObject *py_object_result;
  Config config;
  Result result;

  if (!PyArg_ParseTuple(argv, "O", &py_object_config)) {
    REPORTER("Parse python tuple fail");
    return generate_result(&result);
  }
  if (!PyDict_Check(py_object_config)) {
    REPORTER("Parse python tuple fail");
    return generate_result(&result);
  }

  if (generate_config(&config, py_object_config)) {
    REPORTER("Generate config from python fail");
    return generate_result(&result);
  }

  result = run(&config);

  py_object_result = generate_result(&result);
  delete_all(&result, &config);

  return py_object_result;
}

static PyMethodDef CodeNutJudge_Methods[] = {{"run", python_run, METH_VARARGS},
                                             {NULL, NULL, 0}};

#define GETSTATE(m) ((struct module_state *)PyModule_GetState(m))
#define INITERROR return NULL

struct module_state {
  PyObject *error;
};

static int CodeNutJudge_traverse(PyObject *m, visitproc visit, void *arg) {
  Py_VISIT(GETSTATE(m)->error);
  return 0;
}

static int CodeNutJudge_clear(PyObject *m) {
  Py_CLEAR(GETSTATE(m)->error);
  return 0;
}

static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,       "CodeNutJudge",       NULL,
    sizeof(struct module_state), CodeNutJudge_Methods, NULL,
    CodeNutJudge_traverse,       CodeNutJudge_clear,   NULL};

PyMODINIT_FUNC PyInit_CodeNutJudge(void) {
  PyObject *module = PyModule_Create(&moduledef);

  if (module == NULL)
    INITERROR;
  struct module_state *st = GETSTATE(module);

  st->error = PyErr_NewException("CodeNutJudge.Error", NULL, NULL);
  if (st->error == NULL) {
    Py_DECREF(module);
    INITERROR;
  }
  return module;
}
