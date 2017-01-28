

#calss header
class _PRIVILEGED():
	def __init__(self,): 
		self.name = "PRIVILEGED"
		self.definitions = [u'having a privilege: ', u'Priviledged information is secret and does not have to be given even in a law court.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
