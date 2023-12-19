from rpy2.robjects import r
from rpy2.robjects.packages import importr
r['load']("model_c50.rds")
c50 = importr("C50")
model = r['readRDS']("model_c50.rds")
