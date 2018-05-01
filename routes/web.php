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
    $router->get('filials/{bin}', 'CompanyController@getFilials');
    $router->get('head/{bin}', 'CompanyController@getHead');
    $router->get('wanted/{bin}', 'CompanyController@wanted');

    $router->get('get_token', 'Controller@getToken');
    $router->get('get_auth_status', 'Controller@getAuthStatus');
});

Auth::routes();

Route::get('/home', 'HomeController@index')->name('home');
