

#calss header
class _PHILOSOPHICAL():
	def __init__(self,): 
		self.name = "PHILOSOPHICAL"
		self.definitions = [u'relating to the study or writing of philosophy: ', u'If you are philosophical in your reaction to something that is not satisfactory, you accept it calmly and without anger, understanding that failure and disappointment are a part of life.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
