<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;
use Illuminate\Support\Facades\Schema;

class UpdateInterprises extends Command
{
    /**
     * The name and signature of the console command.
     *
     * @var string
     */
     protected $signature = 'make:UpdateInterprises';

    /**
     * The console command description.
     *
     * @var string
     */
     protected $description = 'Обновить базу данных предприятий на текущий день';

    /**
     * Create a new command instance.
     *
     * @return void
     */
    public function __construct()
    {
        parent::__construct();
    }

    /**
     * Execute the console command.
     *
     * @return mixed
     */
    public function handle()
    {
//        echo PHP_OS;
        $host = env('DB_HOST');
        $db = env('DB_DATABASE');
        $user = env('DB_USERNAME');
        $pass = env('DB_PASSWORD');

        if($pass == ''){
            $pass = 'nopass';
        }



        if (is_dir('interprises_parsers/parsers/legal_entity/files')) {
            shell_exec('rm2 -rf interprises_parsers/parsers/legal_entity/files');
        }
        if (is_dir('interprises_parsers/tmp')) {
            shell_exec('rm2 -rf interprises_parsers/tmp');
        }


        Schema::dropIfExists('legal_branche');
        Schema::dropIfExists('legal_entity');
        Schema::dropIfExists('lie_entity');
        Schema::dropIfExists('exbankrot_entity');
        Schema::dropIfExists('bankrot_entity');
        Schema::dropIfExists('old_entity');
        Schema::dropIfExists('old_branche');
        Schema::dropIfExists('terror_entity');
        Schema::dropIfExists('bad_entity');
        Schema::dropIfExists('good_entity');


        if(PHP_OS == 'WINNT'){
            $output = shell_exec('python interprises_parsers/parsers/legal_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;
            $output = shell_exec('python interprises_parsers/parsers/lie_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;
            $output = shell_exec('python interprises_parsers/parsers/exbankrot_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;
            $output = shell_exec('python interprises_parsers/parsers/bankrot_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;
            $output = shell_exec('python interprises_parsers/parsers/old_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;
            $output = shell_exec('python interprises_parsers/parsers/terror_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;
            $output = shell_exec('python interprises_parsers/parsers/bad_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;
            $output = shell_exec('python interprises_parsers/parsers/good_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;
        } else {
            $output = shell_exec('python3 interprises_parsers/parsers/legal_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;
            $output = shell_exec('python3 interprises_parsers/parsers/lie_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;
            $output = shell_exec('python3 interprises_parsers/parsers/exbankrot_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;
            $output = shell_exec('python3 interprises_parsers/parsers/bankrot_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;
            $output = shell_exec('python3 interprises_parsers/parsers/old_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;
            $output = shell_exec('python3 interprises_parsers/parsers/terror_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;
            $output = shell_exec('python3 interprises_parsers/parsers/bad_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;
            $output = shell_exec('python3 interprises_parsers/parsers/good_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;
        }
    }
}