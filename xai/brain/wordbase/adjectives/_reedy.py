

#calss header
class _REEDY():
	def __init__(self,): 
		self.name = "REEDY"
		self.definitions = [u'A reedy place has many reeds (= tall plants like grass): ', u'A reedy sound, especially a voice, is thin and high and not pleasant to listen to.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
