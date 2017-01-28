

#calss header
class _ROMANTIC():
	def __init__(self,): 
		self.name = "ROMANTIC"
		self.definitions = [u'relating to love or a close loving relationship: ', u'exciting and mysterious and having a strong effect on your emotions: ', u'not practical and having a lot of ideas that are not related to real life: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
