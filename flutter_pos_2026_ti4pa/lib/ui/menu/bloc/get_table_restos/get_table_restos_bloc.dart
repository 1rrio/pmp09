import 'package:bloc/bloc.dart';
import 'package:flutter_pos_2026_ti4pa/data/models/table_resto_model.dart';
import 'package:meta/meta.dart';

part 'get_table_restos_event.dart';
part 'get_table_restos_state.dart';

class GetTableRestosBloc extends Bloc<GetTableRestosEvent, GetTableRestosState> {
  GetTableRestosBloc() : super(GetTableRestosInitial()) {
    on<GetTableRestosEvent>((event, emit) {
      // TODO: implement event handler
    });
  }
}
