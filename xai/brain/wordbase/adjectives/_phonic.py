

#calss header
class _PHONIC():
	def __init__(self,): 
		self.name = "PHONIC"
		self.definitions = [u'using phonics as a method of teaching people to read: ', u'relating to the sounds made in speech, or to the study of these sounds: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
