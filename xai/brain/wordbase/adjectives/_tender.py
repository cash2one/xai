

#calss header
class _TENDER():
	def __init__(self,): 
		self.name = "TENDER"
		self.definitions = [u'gentle, loving, or kind: ', u'(of part of the body) painful, sore, or uncomfortable when touched: ', u'(of meat or vegetables) easy to cut or chew (= crush with the teeth): ', u'Tender plants are easily damaged by cold weather.', u'young: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
