import 'package:flutter/material.dart';

class TableRestoPage extends StatefulWidget {
  const TableRestoPage({super.key});

  @override
  State<TableRestoPage> createState() => _TableRestoPageState();
}

class _TableRestoPageState extends State<TableRestoPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(title: Text('Table Resto'),),);
  }
}
