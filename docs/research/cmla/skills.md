# Design Source for Evaluation CMLA Model

## 1. Structure folder results

```cmd
results
    - cmla
        - 20260101_0101-cmla-resnet50
            - bva
            - hicervix
            - ...
            - ...
    - baseline
        - 20260101_0101-baseline-resnet50
            - bve 
            - hivervix
            - ...
            - ...
```

## 2. Loop in evaluation models

1. Defined path to results for each run experiment:

- `path_to_folder` = 'results/'
- `arch` = ['cmla', 'baseline']
- `source` = ['bva', 'hicervix', 'herlev', 'mendeley_lbc', 'sipakmed', 'all']
- `path_to_subfolder` = [os.listdir(os.path.join(path_to_folder, arch, source))]
- `path_to_results` = path_to_subfolder / metrics / score.json

2. Description the json results file to `path_to_resuls`

* For the baseline model

```python ""
{
    "total_loss": 0.47455403208732605, #total loss of model

    #evaluation model per task
    "stages": {
        #binary classification (0:normal and 1:abnormal)
        "s1": {
            "acc": 0.9997029304504395,
            "f1": 0.999851405620575,
            "pre": 1.0,
            "rec": 0.9997029304504395
        }
    },
    #multi-label classification in list k class with k=(0, 1, 2, 3, 4, 5)
    "end_to_end": {
        "acc": 0.6016042828559875,
        "f1": 0.5169628858566284,
        "pre": 0.5172667503356934,
        "rec": 0.5183230638504028
    }
}
```

* For the cmla model

```python
{
    "total_loss": 0.893283232099023, #total loss of model

    #eval model per task
    "stages": {
        #binary classification
        "s1": {
            "loss": 0.0024493273813277483,
            "acc": 1.0,
            "f1": 1.0,
            "pre": 1.0,
            "rec": 1.0
        },
        #binarcy classification (high and low)
        "s2": {
            "loss": 0.2558513283729553,
            "acc": 0.8969102501869202,
            "f1": 0.9170054793357849,
            "pre": 0.9076704382896423,
            "rec": 0.9265345335006714
        },
        "s3_low": {
            "loss": 0.5999347567558289,
            "acc": 0.6831148862838745,
            "f1": 0.6728262901306152,
            "pre": 0.6812000870704651,
            "rec": 0.6718800067901611
        },
        "s3_high": {
            "loss": 0.6569255590438843,
            "acc": 0.6863219141960144,
            "f1": 0.7037477493286133,
            "pre": 0.7062142491340637,
            "rec": 0.7091979384422302
        }
    },
    "s3_loss_weighted": 0.63498257634474,
    #multi-label classification same as the baseline model
    "end_to_end": {
        "acc": 0.6164587140083313,
        "f1": 0.627838134765625,
        "pre": 0.6329250335693359,
        "rec": 0.6296854019165039
    }
}
```

## 3. Design pipeline
   
For loop read score.json and extract each metrics (only binary classification and multi-label classification), next s2_low, s2_high and s3 ...) on across , dataset sources and run_exp.

1. Example pipeline for run_exp = 20260101_0101-cmla-resnet50 with arch = baseline

- Read score.json from `path_to_json` then extract results in this file. Each metric as acc, f1, pre, rec get values by dot 100 and use :2.f (or round(value, 2)). Score format:

```python
{
    "binary": {
        "acc": 61.64,
        "f1": 62.78,
        "pre": 63.29,
        "rec": 62.96
    },
    "multi": {
        "acc": same binary
    }
}
```

- Repeat on across run_exp then return file results call the name "all_results.json" below:

```python
{
    "run_id (example: 20260101_0101-cmla-resnet50)": 
    {
        "source": (exmaple: bva, hicervix v.v)
        "binary": {
            "acc": 61.64,
            "f1": 62.78,
            "pre": 63.29,
            "rec": 62.96
        },
        "multi": {
            "acc": same binary
        }
    },

    #run_id next v.v.
}
```

- Compute mean & covariance then previous step completed. Using numpy or pandas for mean and std all run_exp, return format below and fil to bottom file `results_all.json`

```python
{
    "run_id": {
        "source": bva, hicervix ...
        "binary": {
            "acc": {
                "mean" : 67.67,
                "std" : 0.23
            },
            "f1": {
                "mean" : 67.67,
                "std" : 0.23
            },
            "pre": {
                "mean" : 67.67,
                "std" : 0.23
            },
            "rec": {
                "mean" : 67.67,
                "std" : 0.23
            }
        },

        "multi": {
            "acc" v.v
        }
    },

    #next run_id
}
```

- Replace `arch`=baseline by cmla then loop and process as baseline


## 4. Structure folder final

We want structure folder final has fomat as:

```cmd
results
    - cmla
        - 20260101_0101-cmla-resnet50
            - bva
            - hicervix
            - ...
            - ...
        - ...
        - results_all.json
    - baseline
        - 20260101_0101-baseline-resnet50
            - bva 
            - hivervix
            - ...
            - ...
        - ... 
        - results_all.json
```

## 5. Results and Reports

Then the pipeline extract and export results to file results_all.json completed. Next step read those file results and writting report.

**Preliminaries.** Both results.json of the baseline and cmla model is same, format below. 

```python
{
    "all": {
        "binary": {
            "acc": {
                "mean": 93.92,
                "std": 0.09
            },
            "f1": {
                "mean": 96.55,
                "std": 0.05
            },
            "pre": {
                "mean": 99.96,
                "std": 0.02
            },
            "rec": {
                "mean": 93.38,
                "std": 0.09
            }
        },
        "multi": {
            "acc": {
                "mean": 68.28,
                "std": 1.38
            },
            "f1": {
                "mean": 71.9,
                "std": 1.13
            },
            "pre": {
                "mean": 71.78,
                "std": 0.89
            },
            "rec": {
                "mean": 72.22,
                "std": 1.32
            }
        }
    },
    "bva": {
        "binary": {
            "acc": {
                "mean": 99.98,
                "std": 0.02
            },
            "f1": {
                "mean": 99.99,
                "std": 0.01
            },
            "pre": {
                "mean": 100.0,
                "std": 0.0
            },
            "rec": {
                "mean": 99.98,
                "std": 0.02
            }
        },
        "multi": {
            "acc": {
                "mean": 62.03,
                "std": 1.27
            },
            "f1": {
                "mean": 57.01,
                "std": 5.75
            },
            "pre": {
                "mean": 56.76,
                "std": 5.82
            },
            "rec": {
                "mean": 57.56,
                "std": 5.84
            }
        }
    },
    "herlev": {
        "binary": {
            "acc": {
                "mean": 29.28,
                "std": 2.2
            },
            "f1": {
                "mean": 11.99,
                "std": 4.65
            },
            "pre": {
                "mean": 77.61,
                "std": 16.2
            },
            "rec": {
                "mean": 6.54,
                "std": 2.67
            }
        },
        "multi": {
            "acc": {
                "mean": 95.0,
                "std": 3.04
            },
            "f1": {
                "mean": 39.14,
                "std": 13.91
            },
            "pre": {
                "mean": 40.0,
                "std": 13.69
            },
            "rec": {
                "mean": 38.33,
                "std": 14.07
            }
        }
    },
    "hicervix": {
        "binary": {
            "acc": {
                "mean": 99.97,
                "std": 0.04
            },
            "f1": {
                "mean": 99.98,
                "std": 0.02
            },
            "pre": {
                "mean": 100.0,
                "std": 0.0
            },
            "rec": {
                "mean": 99.97,
                "std": 0.04
            }
        },
        "multi": {
            "acc": {
                "mean": 71.72,
                "std": 2.39
            },
            "f1": {
                "mean": 67.14,
                "std": 8.24
            },
            "pre": {
                "mean": 67.65,
                "std": 7.69
            },
            "rec": {
                "mean": 66.99,
                "std": 8.4
            }
        }
    },
    "mendeley_lbc": {
        "binary": {
            "acc": {
                "mean": 99.73,
                "std": 0.61
            },
            "f1": {
                "mean": 99.64,
                "std": 0.81
            },
            "pre": {
                "mean": 99.29,
                "std": 1.6
            },
            "rec": {
                "mean": 100.0,
                "std": 0.0
            }
        },
        "multi": {
            "acc": {
                "mean": 96.3,
                "std": 1.58
            },
            "f1": {
                "mean": 92.13,
                "std": 2.72
            },
            "pre": {
                "mean": 91.49,
                "std": 3.03
            },
            "rec": {
                "mean": 93.87,
                "std": 1.87
            }
        }
    },
    "sipakmed": {
        "binary": {
            "acc": {
                "mean": 60.66,
                "std": 0.59
            },
            "f1": {
                "mean": 5.35,
                "std": 2.73
            },
            "pre": {
                "mean": 100.0,
                "std": 0.0
            },
            "rec": {
                "mean": 2.77,
                "std": 1.45
            }
        },
        "multi": {
            "acc": {
                "mean": 100.0,
                "std": 0.0
            },
            "f1": {
                "mean": 100.0,
                "std": 0.0
            },
            "pre": {
                "mean": 100.0,
                "std": 0.0
            },
            "rec": {
                "mean": 100.0,
                "std": 0.0
            }
        }
    }
}
```

Now, I'm design pipeline step-by-step:

- `path_to_json` = `./results_all.json`
- With each results.json of model, using json to load file and flatten json to dataframe includes all infomation in json and addition key model (cmla or baseline corresponding). Continue, using pivot follow columns equal datasets source key (all, bva, hicervix...).
- Using method `.to_markdown` of python converts dataframe pivoted to markdown templates for support writting report markdown final.
- Return two file markdown table teamplate of both baseline and cmla model.
- Finally, groupby and custom returns only table. This table sorted follows key model and task. Format the report table as:

| Model | Task | Metrics | All | BVA | ... |
| :--:  | :--: | :---: | :--: | :--: | :--: |
| baseline | binary | acc | 90.90 | 80.80 | ... |
| baseline | binary | f1 | 90.90 | 80.80 | ... |
| baseline | binary | pre | 90.90 | 80.80 | ... |
| baseline | binary | rec | 90.90 | 80.80 | ... |
| cmla  | binary | acc | 90.90 | 80.80 | ... |
| cmla  | binary | f1 | 90.90 | 80.80 | ... |
| cmla  | binary | pre | 90.90 | 80.80 | ... |
| cmla  | binary | rec | 90.90 | 80.80 | ... |
|   |  |  |  |  |  |
| baseline | multi | acc | 90.90 | 80.80 | ... |
| baseline | multi | f1 | 90.90 | 80.80 | ... |
| baseline | multi | pre | 90.90 | 80.80 | ... |
| baseline | multi | rec | 90.90 | 80.80 | ... |
| cmla  | multi | acc | 90.90 | 80.80 | ... |
| cmla  | multi | f1 | 90.90 | 80.80 | ... |
| cmla  | multi | pre | 90.90 | 80.80 | ... |
| cmla  | multi | rec | 90.90 | 80.80 | ... |


## Data Visualization

When the evaluation protocol for the baseline anh CMLA model completed, let brainstorming about data visualization on those reults. Below, step by step the practical:

- Thinking and recomment all type plot benifit for presentation results in paper is clear and academic. Return a list plot and explain why choose it? Example:

```text
1. Barchart.
    - Objectives: Comparation performance (f1_score) between the base line model and cmla model for each datasets as bva, hicervix, mendeleyLBC v.v.
    - Implementations and Setup config ...
    
2. ...
```

- Using seaborn or maplotlib is tools draw (or other framework). All source ussing function and class and show all config if you setup addition explain detail about parameter. Example:

```python
# setup rcParams in matplotlib
    plt.rcParams.update({
            "font.family": "serif",
            "font.serif": ["Times New Roman", "DejaVu Serif"],
            "font.size": 10,
            "axes.labelsize": 11,
            "axes.titlesize": 12,
            "legend.fontsize": 10,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "grid.alpha": 0.3,
            "grid.linestyle": "--",
            "savefig.dpi": 300,
            "savefig.bbox": "tight"
        })
```

- The firts, you need focus and practical all step previous for export and show all plan of you comment. If im argee plan is continue bellow.

## Appendix A: Structure Folder

## Appendix B: File Json Results 

## Appendix C: Futher Reading

## Appendix D: Response Approach