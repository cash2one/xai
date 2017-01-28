

#calss header
class _SETTLED():
	def __init__(self,): 
		self.name = "SETTLED"
		self.definitions = [u'If you feel settled in a job, school, etc., you have become familiar with it and are comfortable and happy there: ', u'living somewhere, especially permanently: ', u'Settled weather is calm and unlikely to change: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
