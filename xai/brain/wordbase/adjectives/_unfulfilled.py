

#calss header
class _UNFULFILLED():
	def __init__(self,): 
		self.name = "UNFULFILLED"
		self.definitions = [u'If a wish, hope, promise, etc. is unfulfilled, it has not happened or been achieved: ', u'unhappy because you think you should be achieving more in your life']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
