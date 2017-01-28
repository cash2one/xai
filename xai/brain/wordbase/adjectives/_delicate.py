

#calss header
class _DELICATE():
	def __init__(self,): 
		self.name = "DELICATE"
		self.definitions = [u'needing careful treatment, especially because easily damaged: ', u'needing to be done carefully: ', u'a situation. matter, etc. that needs to be dealt with carefully in order to avoid trouble or offence: ', u'able to measure very small changes: ', u'pleasantly soft or light: ', u'having a thin, attractive shape: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
