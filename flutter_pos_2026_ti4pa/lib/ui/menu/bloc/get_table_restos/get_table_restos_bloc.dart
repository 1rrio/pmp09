import 'package:bloc/bloc.dart';
import 'package:flutter_pos_2026_ti4pa/data/models/table_resto_model.dart';
import 'package:flutter_pos_2026_ti4pa/data/repo/table_resto_repository.dart';
import 'package:meta/meta.dart';

part 'get_table_restos_event.dart';
part 'get_table_restos_state.dart';

class GetTableRestosBloc extends Bloc<GetTableRestosEvent, GetTableRestosState> {
  final tableRestoRepository = TableRestoRepository();
  GetTableRestosBloc() : super(GetTableRestosInitial()) {
    on<TableRestoFetched>((event, emit) async{
      emit(GetTableRestosLoading());
      try{
        var response = await tableRestoRepository.getAllTableResto();
        emit(GetTableRestosLoaded(list: response));
      }catch(e){
        emit(GetTableRestosError(message: e.toString()));
      }
    });
  }
}
