import 'package:dio/dio.dart';
import 'package:flutter/material.dart';
import 'package:flutter_pos_2026_ti4pa/data/models/table_resto_model.dart';
import 'package:flutter_pos_2026_ti4pa/core/api_client.dart';

class TableRestoRepository extends ApiClient {
  Future<List<TableRestoModel>> getAllTableResto() async {
    try {
      var response = await dio.get('table-restos');
      debugPrint('GET ALL Table Resto : ${response.data}');
      List list = response.data;
      List<TableRestoModel> listTableResto = list
          .map((element) => TableRestoModel.fromJson(element))
          .toList();
      return listTableResto;
    } on DioException catch (e) {
      throw Exception(e);
    }
  }
}

