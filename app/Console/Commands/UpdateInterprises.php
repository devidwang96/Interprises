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
        $host = env('DB_HOST');
        $db = env('DB_DATABASE');
        $user = env('DB_USERNAME');
        $pass = env('DB_PASSWORD');

        if ($pass == '') {
            $pass = 'nopass';
        }

        if(PHP_OS == 'WINNT'){
            if (is_dir('interprises_parsers/parsers/legal_entity/files')) {
                shell_exec('rm2 -rf interprises_parsers/parsers/legal_entity/files');
            }

            if (is_dir('interprises_parsers/tmp')) {
                shell_exec('rm2 -rf interprises_parsers/tmp');
            }
        } else {
            if (is_dir('interprises_parsers/parsers/legal_entity/files')) {
                shell_exec('rm -rf interprises_parsers/parsers/legal_entity/files');
            }

            if (is_dir('interprises_parsers/tmp')) {
                shell_exec('rm -rf interprises_parsers/tmp');
            }
        }


        Schema::dropIfExists('legal_branche');
        Schema::dropIfExists('filials');
        Schema::dropIfExists('legal_entity');
        Schema::dropIfExists('lie_entity');
        Schema::dropIfExists('exbankrot_entity');
        Schema::dropIfExists('bankrot_entity');
        Schema::dropIfExists('terror_entity');
        Schema::dropIfExists('bad_entity');
        Schema::dropIfExists('good_entity');
        Schema::dropIfExists('old_entity');
        Schema::dropIfExists('old_branche');
        Schema::dropIfExists('legal_entity_history');
        Schema::dropIfExists('kato');
        Schema::dropIfExists('oked');
        Schema::dropIfExists('promiser_entity');
        Schema::dropIfExists('codex_entity');
        Schema::dropIfExists('jur_exist_entity');

        if (PHP_OS == 'WINNT') {
            $output = shell_exec('python interprises_parsers/parsers/legal_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;

            $output = shell_exec('python interprises_parsers/parsers/legal_entity/filials.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;

            $output = shell_exec('python interprises_parsers/parsers/lie_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;

            $output = shell_exec('python interprises_parsers/parsers/exbankrot_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;

            $output = shell_exec('python interprises_parsers/parsers/bankrot_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;

            $output = shell_exec('python interprises_parsers/parsers/terror_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;

            $output = shell_exec('python interprises_parsers/parsers/bad_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;

            $output = shell_exec('python interprises_parsers/parsers/good_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;

            $output = shell_exec('python interprises_parsers/parsers/old_entity/init-changes.py ' . $host . ' ' . $user . ' ' . $pass . ' ' . $db);
            echo $output;

            $output = shell_exec('python interprises_parsers/parsers/kato/kato.py ' . $host . ' ' . $user . ' ' . $pass . ' ' . $db);
            echo $output;

            $output = shell_exec('python interprises_parsers/parsers/oked/oked.py ' . $host . ' ' . $user . ' ' . $pass . ' ' . $db);
            echo $output;

            $output = shell_exec('python interprises_parsers/parsers/promiser_entity/promiser.py ' . $host . ' ' . $user . ' ' . $pass . ' ' . $db);
            echo $output;

            $output = shell_exec('python interprises_parsers/parsers/codex_entity/codex.py ' . $host . ' ' . $user . ' ' . $pass . ' ' . $db);
            echo $output;

            $output = shell_exec('python interprises_parsers/parsers/jur_exist_entity/jur_exist.py ' . $host . ' ' . $user . ' ' . $pass . ' ' . $db);
            echo $output;
        } else {
            $output = shell_exec('python3 interprises_parsers/parsers/legal_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;

            $output = shell_exec('python3 interprises_parsers/parsers/legal_entity/filials.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;

            $output = shell_exec('python3 interprises_parsers/parsers/lie_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;

            $output = shell_exec('python3 interprises_parsers/parsers/exbankrot_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;

            $output = shell_exec('python3 interprises_parsers/parsers/bankrot_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;

            $output = shell_exec('python3 interprises_parsers/parsers/terror_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;

            $output = shell_exec('python3 interprises_parsers/parsers/bad_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;

            $output = shell_exec('python3 interprises_parsers/parsers/good_entity/stat_list.py '.$host.' '.$user.' '.$pass.' '.$db);
            echo $output;

            $output = shell_exec('python3 interprises_parsers/parsers/old_entity/init-changes.py ' . $host . ' ' . $user . ' ' . $pass . ' ' . $db);
            echo $output;

            $output = shell_exec('python3 interprises_parsers/parsers/kato/kato.py ' . $host . ' ' . $user . ' ' . $pass . ' ' . $db);
            echo $output;

            $output = shell_exec('python3 interprises_parsers/parsers/oked/oked.py ' . $host . ' ' . $user . ' ' . $pass . ' ' . $db);
            echo $output;

            $output = shell_exec('python3 interprises_parsers/parsers/promiser_entity/promiser.py ' . $host . ' ' . $user . ' ' . $pass . ' ' . $db);
            echo $output;

            $output = shell_exec('python3 interprises_parsers/parsers/codex_entity/codex.py ' . $host . ' ' . $user . ' ' . $pass . ' ' . $db);
            echo $output;

            $output = shell_exec('python3 interprises_parsers/parsers/jur_exist_entity/jur_exist.py ' . $host . ' ' . $user . ' ' . $pass . ' ' . $db);
            echo $output;

        }
    }
}


