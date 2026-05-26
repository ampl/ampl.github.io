# AMPLS Libraries Changelog

## 20260526

### 0.2.4
- **[New]** Python: added support for pyinstaller
- **[New]** Python: updated packages and solver libs for all distributed solvers. 
- **[New]** Python: support for Python versions > 3.12


## 20260408

### 0.2.3
* **[Breaking]** Python: the injected class method `amplpy.AMPL.import_solution ` is now called `amplpy.AMPL.import_ampls_solution`


## 20241115

### 0.2.2
* **[New]** Updated Gurobi to 12.0

## 20240731

### 0.2.1
* **[New]** CPLEXCallback: addLazy and addCut now support an optional parameter local, specifying
            if the added constraint is locally valid (value = 1) or globally valid (value = 0 - default)
* **[Fix]** Python: fixed an issue arising when inheriting from solver-specific callback classes

## 20240327

### 0.2.0
* **[New]** Python: Added `Constraint.to_string` and `AMPLModel.add_constraint`

## 20240319

### 0.1.9
* **[New]** Python: added parameter `import_entities` to the method `amplpy.AMPL.import_solution` to 
            import entities added via AMPLS back to the amplpy model
  

## 20240316

### 0.1.8
* **[New]** Python: added parameter `keep_files` to the method `amplpy.AMPL.import_solution` that
            if set to true, keeps the exported row, col and NL files 
  
## 20240113

### 0.1.7

* **[[Fix]]** Row and column files written to the temporary directory when exporting from AMPLAPI 
            or amplpy are now removed

## 20231219

### 0.1.6

* **[New]** Added Python examples in python/examples
* **[Fix]** Python: `get_solution_dict` and `getSolutionDict`

## 20231120

### 0.1.5

* **[Fix]** Gurobi: getting solution vector and objective bounds in callbacks at MIPSOL and MIPNODE

## 20230809

### 0.1.4

* **[New]** Added SolverAttributes::INT_NumIntegerVars
* **[Fix]** Various bug fixes

## 20230627

### 0.1.3

* **[Breaking]** ampls::CPLEXCallback is now using the generic callbacks. Note that multithreading 
  is not disabled by default but implementation needs extra care. 
* **[Breaking]** Solver and solver driver related errors in Python are now thrown as ampls.AMPLSolverException
* **[Fix]** Fixed python wrappers for AMPLModel.*etAMPLParameter and AMPLModel.getStatus
* **[New]** Added AMPLModel::infinity() and AMPLModel::negInfinity() to use when creating new entities
  with no bounds
* **[Fix]** A problem arising when replaying in AMPL new entities recorded with AMPLModel::record()
* **[Fix]** Mapping of callback information in BaseCallback::getValue()

## 20230602

### 0.1.2

* **[New]** Added parameter to `AMPLModel::load()` and `AMPLAPIInterface::exportModel<T>()`
  to specify options when loading the model. Necessary for options that involve the solver 
  driver 
* **[Breaking]** Renamed `BaseCallback::checkCanDo` to `canDo`
* *Options handling*: 
  
  * **[Breaking]** Renamed the function `AMPLModel::getIntOptionValue` to `AMPLModel::getIntOption`
  * **[New]** Implemented `AMPLModel::getDoubleOption` and `AMPLModel::getStringOption`

