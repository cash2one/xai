

#calss header
class _FRONTAL():
	def __init__(self,): 
		self.name = "FRONTAL"
		self.definitions = [u'relating to the front of something: ', u'relating to the forehead (= the flat part of the face, above the eyes and below the hair)', u'very strong criticism of someone or something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
