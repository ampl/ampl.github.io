# BARON Changelog


## 20241119
- Beta release of MP driver for Baron, use with option `option solver baronmp;`,
  to use the original ASL driver use `option solver baron;`
- Breaking changes with ASL driver:
  - `version` keyword removed
  - Changed behaviour of the `iisfind` option to be consistent with MP features;
    see `alg:iisfind`, `alg:iismethod`, `alg:iisint`
  - Absolute values are reformulated as MIP instead of abs(x)=(x^2)^0.5
  - Added option value `local` to `scratch` that automatically places the scratch 
    files in a directory with the name derived from the model file (e.g. for 
    `/test/model.nl` the directory will be `/test/model.nl_baron/`)