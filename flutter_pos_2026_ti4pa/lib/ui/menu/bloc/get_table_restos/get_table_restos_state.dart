part of 'get_table_restos_bloc.dart';

@immutable
sealed class GetTableRestosState {}

final class GetTableRestosInitial extends GetTableRestosState {}

final class GetTableRestosLoading extends GetTableRestosState {}

final class GetTableRestosLoaded extends GetTableRestosState {
  final List<TableRestoModel> list;

  GetTableRestosLoaded({required this.list});
}

final class GetTableRestosError extends GetTableRestosState {
  final String message;

  GetTableRestosError({required this.message});
}

