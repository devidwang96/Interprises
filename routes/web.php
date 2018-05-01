<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('app');
});

Route::group(['prefix' => 'backend'], function ($router) {
    $router->get('search/{query}', 'SearchController@index');
    $router->get('company/{bin}', 'CompanyController@index');
    $router->get('history/{bin}', 'HistoryController@index');
    $router->get('kato/{kato}', 'CompanyController@getKato');
    $router->get('oked/{oked}', 'CompanyController@getOked');
});