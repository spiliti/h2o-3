#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# This file is auto-generated by h2o-3/h2o-bindings/bin/gen_python.py
# Copyright 2016 H2O.ai;  Apache License Version 2.0 (see LICENSE for details)
#
from __future__ import absolute_import, division, print_function, unicode_literals

from h2o.estimators.estimator_base import H2OEstimator
from h2o.exceptions import H2OValueError
from h2o.frame import H2OFrame
from h2o.utils.typechecks import assert_is_type, Enum, numeric, is_type
import json
import ast


class H2OStackedEnsembleEstimator(H2OEstimator):
    """
    Stacked Ensemble

    Builds a stacked ensemble (aka "super learner") machine learning method that uses two
    or more H2O learning algorithms to improve predictive performance. It is a loss-based
    supervised learning method that finds the optimal combination of a collection of prediction
    algorithms.This method supports regression and binary classification.

    Examples
    --------
      >>> import h2o
      >>> h2o.init()
      >>> from h2o.estimators.random_forest import H2ORandomForestEstimator
      >>> from h2o.estimators.gbm import H2OGradientBoostingEstimator
      >>> from h2o.estimators.stackedensemble import H2OStackedEnsembleEstimator
      >>> col_types = ["numeric", "numeric", "numeric", "enum", "enum", "numeric", "numeric", "numeric", "numeric"]
      >>> data = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/prostate/prostate.csv", col_types=col_types)
      >>> train, test = data.split_frame(ratios=[.8], seed=1)
      >>> x = ["CAPSULE","GLEASON","RACE","DPROS","DCAPS","PSA","VOL"]
      >>> y = "AGE"
      >>> nfolds = 5
      >>> my_gbm = H2OGradientBoostingEstimator(nfolds=nfolds, fold_assignment="Modulo", keep_cross_validation_predictions=True)
      >>> my_gbm.train(x=x, y=y, training_frame=train)
      >>> my_rf = H2ORandomForestEstimator(nfolds=nfolds, fold_assignment="Modulo", keep_cross_validation_predictions=True)
      >>> my_rf.train(x=x, y=y, training_frame=train)
      >>> stack = H2OStackedEnsembleEstimator(model_id="my_ensemble", training_frame=train, validation_frame=test, base_models=[my_gbm.model_id, my_rf.model_id])
      >>> stack.train(x=x, y=y, training_frame=train, validation_frame=test)
      >>> stack.model_performance()
    """

    algo = "stackedensemble"

    def __init__(self, **kwargs):
        super(H2OStackedEnsembleEstimator, self).__init__()
        self._parms = {}
        names_list = {"model_id", "training_frame", "response_column", "validation_frame", "blending_frame",
                      "base_models", "metalearner_algorithm", "metalearner_nfolds", "metalearner_fold_assignment",
                      "metalearner_fold_column", "metalearner_params", "categorical_encoding", "seed",
                      "keep_levelone_frame", "export_checkpoints_dir"}
        if "Lambda" in kwargs: kwargs["lambda_"] = kwargs.pop("Lambda")
        for pname, pvalue in kwargs.items():
            if pname == 'model_id':
                self._id = pvalue
                self._parms["model_id"] = pvalue
            elif pname in names_list:
                # Using setattr(...) will invoke type-checking of the arguments
                setattr(self, pname, pvalue)
            else:
                raise H2OValueError("Unknown parameter %s = %r" % (pname, pvalue))
        self._parms["_rest_version"] = 99

    @property
    def training_frame(self):
        """
        Id of the training data frame.

        Type: ``H2OFrame``.
        """
        return self._parms.get("training_frame")

    @training_frame.setter
    def training_frame(self, training_frame):
        assert_is_type(training_frame, None, H2OFrame)
        self._parms["training_frame"] = training_frame


    @property
    def response_column(self):
        """
        Response variable column.

        Type: ``str``.
        """
        return self._parms.get("response_column")

    @response_column.setter
    def response_column(self, response_column):
        assert_is_type(response_column, None, str)
        self._parms["response_column"] = response_column


    @property
    def validation_frame(self):
        """
        Id of the validation data frame.

        Type: ``H2OFrame``.
        """
        return self._parms.get("validation_frame")

    @validation_frame.setter
    def validation_frame(self, validation_frame):
        assert_is_type(validation_frame, None, H2OFrame)
        self._parms["validation_frame"] = validation_frame


    @property
    def blending_frame(self):
        """
        Frame used to compute the predictions that serve as the training frame for the metalearner (triggers blending
        mode if provided)

        Type: ``H2OFrame``.
        """
        return self._parms.get("blending_frame")

    @blending_frame.setter
    def blending_frame(self, blending_frame):
        assert_is_type(blending_frame, None, H2OFrame)
        self._parms["blending_frame"] = blending_frame


    @property
    def base_models(self):
        """
        List of models (or model ids) to ensemble/stack together. If not using blending frame, then models must have
        been cross-validated using nfolds > 1, and folds must be identical across models.

        Type: ``List[str]``  (default: ``[]``).
        """
        return self._parms.get("base_models")

    @base_models.setter
    def base_models(self, base_models):
         if is_type(base_models,[H2OEstimator]):
            base_models = [b.model_id for b in base_models]
            self._parms["base_models"] = base_models
         else:
            assert_is_type(base_models, None, [str])
            self._parms["base_models"] = base_models


    @property
    def metalearner_algorithm(self):
        """
        Type of algorithm to use as the metalearner. Options include 'AUTO' (GLM with non negative weights; if
        validation_frame is present, a lambda search is performed), 'glm' (GLM with default parameters), 'gbm' (GBM with
        default parameters), 'drf' (Random Forest with default parameters), or 'deeplearning' (Deep Learning with
        default parameters).

        One of: ``"auto"``, ``"glm"``, ``"gbm"``, ``"drf"``, ``"deeplearning"``  (default: ``"auto"``).
        """
        return self._parms.get("metalearner_algorithm")

    @metalearner_algorithm.setter
    def metalearner_algorithm(self, metalearner_algorithm):
        assert_is_type(metalearner_algorithm, None, Enum("auto", "glm", "gbm", "drf", "deeplearning"))
        self._parms["metalearner_algorithm"] = metalearner_algorithm


    @property
    def metalearner_nfolds(self):
        """
        Number of folds for K-fold cross-validation of the metalearner algorithm (0 to disable or >= 2).

        Type: ``int``  (default: ``0``).
        """
        return self._parms.get("metalearner_nfolds")

    @metalearner_nfolds.setter
    def metalearner_nfolds(self, metalearner_nfolds):
        assert_is_type(metalearner_nfolds, None, int)
        self._parms["metalearner_nfolds"] = metalearner_nfolds


    @property
    def metalearner_fold_assignment(self):
        """
        Cross-validation fold assignment scheme for metalearner cross-validation.  Defaults to AUTO (which is currently
        set to Random). The 'Stratified' option will stratify the folds based on the response variable, for
        classification problems.

        One of: ``"auto"``, ``"random"``, ``"modulo"``, ``"stratified"``.
        """
        return self._parms.get("metalearner_fold_assignment")

    @metalearner_fold_assignment.setter
    def metalearner_fold_assignment(self, metalearner_fold_assignment):
        assert_is_type(metalearner_fold_assignment, None, Enum("auto", "random", "modulo", "stratified"))
        self._parms["metalearner_fold_assignment"] = metalearner_fold_assignment


    @property
    def metalearner_fold_column(self):
        """
        Column with cross-validation fold index assignment per observation for cross-validation of the metalearner.

        Type: ``str``.
        """
        return self._parms.get("metalearner_fold_column")

    @metalearner_fold_column.setter
    def metalearner_fold_column(self, metalearner_fold_column):
        assert_is_type(metalearner_fold_column, None, str)
        self._parms["metalearner_fold_column"] = metalearner_fold_column


    @property
    def metalearner_params(self):
        """
        Parameters for metalearner algorithm

        Type: ``dict``  (default: ``None``).
        Example: metalearner_gbm_params = {'max_depth': 2, 'col_sample_rate': 0.3}
        """
        if self._parms.get("metalearner_params") != None:
            metalearner_params_dict =  ast.literal_eval(self._parms.get("metalearner_params"))
            for k in metalearner_params_dict:
                if len(metalearner_params_dict[k]) == 1: #single parameter
                    metalearner_params_dict[k] = metalearner_params_dict[k][0]
            return metalearner_params_dict
        else:
            return self._parms.get("metalearner_params")

    @metalearner_params.setter
    def metalearner_params(self, metalearner_params):
        assert_is_type(metalearner_params, None, dict)
        if metalearner_params is not None and metalearner_params != "":
            for k in metalearner_params:
                if ("[" and "]") not in str(metalearner_params[k]):
                    metalearner_params[k]=[metalearner_params[k]]
            self._parms["metalearner_params"] = str(json.dumps(metalearner_params))
        else:
            self._parms["metalearner_params"] = None


    @property
    def categorical_encoding(self):
        """
        Encoding scheme for categorical features

        One of: ``"auto"``, ``"enum"``, ``"one_hot_internal"``, ``"one_hot_explicit"``, ``"binary"``, ``"eigen"``,
        ``"label_encoder"``, ``"sort_by_response"``, ``"enum_limited"``  (default: ``"auto"``).
        """
        return self._parms.get("categorical_encoding")

    @categorical_encoding.setter
    def categorical_encoding(self, categorical_encoding):
        assert_is_type(categorical_encoding, None, Enum("auto", "enum", "one_hot_internal", "one_hot_explicit", "binary", "eigen", "label_encoder", "sort_by_response", "enum_limited"))
        self._parms["categorical_encoding"] = categorical_encoding


    @property
    def seed(self):
        """
        Seed for random numbers; passed through to the metalearner algorithm. Defaults to -1 (time-based random number)

        Type: ``int``  (default: ``-1``).
        """
        return self._parms.get("seed")

    @seed.setter
    def seed(self, seed):
        assert_is_type(seed, None, int)
        self._parms["seed"] = seed


    @property
    def keep_levelone_frame(self):
        """
        Keep level one frame used for metalearner training.

        Type: ``bool``  (default: ``False``).
        """
        return self._parms.get("keep_levelone_frame")

    @keep_levelone_frame.setter
    def keep_levelone_frame(self, keep_levelone_frame):
        assert_is_type(keep_levelone_frame, None, bool)
        self._parms["keep_levelone_frame"] = keep_levelone_frame


    @property
    def export_checkpoints_dir(self):
        """
        Automatically export generated models to this directory.

        Type: ``str``.
        """
        return self._parms.get("export_checkpoints_dir")

    @export_checkpoints_dir.setter
    def export_checkpoints_dir(self, export_checkpoints_dir):
        assert_is_type(export_checkpoints_dir, None, str)
        self._parms["export_checkpoints_dir"] = export_checkpoints_dir



    # Print the metalearner of an H2OStackedEnsembleEstimator.
    def metalearner(self):
        model = self._model_json["output"]
        if "metalearner" in model and model["metalearner"] is not None:
            return model["metalearner"]
        print("No metalearner for this model")  

    #Fetch the levelone_frame_id for an H2OStackedEnsembleEstimator.   
    def levelone_frame_id(self):
        model = self._model_json["output"]
        if "levelone_frame_id" in model and model["levelone_frame_id"] is not None:
            return model["levelone_frame_id"]
        print("No levelone_frame_id for this model")         

    def stacking_strategy(self):
        model = self._model_json["output"]
        if "stacking_strategy" in model and model["stacking_strategy"] is not None:
            return model["stacking_strategy"]
        print("No stacking strategy for this model")  

    # Override train method to support blending 
    def train(self, x=None, y=None, training_frame=None, blending_frame=None, **kwargs):
        assert_is_type(blending_frame, None, H2OFrame)

        def extend_parms(parms):
            if blending_frame is not None:
                parms['blending_frame'] = blending_frame

        super(self.__class__, self)._train(x, y, training_frame, extend_parms_fn=extend_parms, **kwargs)
