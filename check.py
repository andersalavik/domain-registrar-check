from email.policy import default
import json
import optparse
import sys
import whois
import optparse
import logging





class CheckDomain(object):
    
    DOMAINS = {}
    
    def __init__(self):
        self.use_qnichost = False
        
    def run(self,options):
        loglevel = options['loglevel']
        numeric_level = getattr(logging, loglevel.upper(), None)
        logging.basicConfig(format='%(levelname)s:%(message)s', level=numeric_level)
        
        
        logging.debug('Started')
        
        domain_list=[]
        if options is None:
            options = {}
        
        logging.debug(options)
        
        if 'domainfile' in options and options['domainfile'] is not None:
            domain_list = self.processDomainListFile(options['domainfile'])
            
        
        
        self.processDomainList(domain_list)
        
        
        if options['json'] is True:
            self.jsonOut()
        logging.debug('Finished')
        

    def domainCheck(self, domain):
        logging.debug('Kontrollerar: %s', domain)
        domain_info = dict()
        
        try:
            
            domainc = whois.whois(domain)
        except:
            logging.debug('Hittar inte')
            domain_info['status'] = 'fail'
            pass
        else:
            logging.debug('Registrar: %s', domainc['registrar'])
            logging.debug('Status: %s', domainc['status'])
            logging.debug('Name server %s:', domainc['name_servers'])
            domain_info['registrar'] = domainc['registrar']
            domain_info['status'] = domainc['status']
            
            servers = list()
            for server in domainc['name_servers']:
                servers.append(server)
            
            domain_info['name_servers'] = servers
        
        
        

        return domain_info
    
    def processDomainListFile(self,file):
        logging.debug('processar domain list file')
        domains = open(file, 'r')
        domains = [line.rstrip('\n') for line in domains]
        
        
        
        return domains
    
    def processDomainList(self,domainlist):
        logging.debug('processar domain list')
        for domain in domainlist:
            self.DOMAINS[domain] = self.domainCheck(domain)
            
    def jsonOut(self):
        logging.debug('Outputs JSON Start')
        print(json.dumps(self.DOMAINS,indent = 4))
        logging.debug('Outputs JSON Stop')
        
            
        
        


def parse_command_line(argv):
    
    usage = "usage: %prog [options] name"
    parser = optparse.OptionParser(add_help_option=False, usage=usage)

    parser.add_option("-f", "--file", action="store",
                      dest="domainfile",type="string",
                      help="Check using file.")
    parser.add_option("-j", "--json", action="store_true",
                      dest="json",default=False,
                      help="Output JSON")
    parser.add_option("--log", action="store",
                      dest="loglevel",type="string",
                      help="--log debug för att skriva ut i console", default="info")

    parser.add_option("-h", "--help", action="help")
    return parser.parse_args(argv)



    

if __name__ == "__main__":

    flags = 0
    domainCheck = CheckDomain()
    options, args = parse_command_line(sys.argv)
    
    domainCheck.run(options.__dict__)

