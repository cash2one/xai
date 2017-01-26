

from xai.brain.wordbase.nouns._testimonial import _TESTIMONIAL

#calss header
class _TESTIMONIALS(_TESTIMONIAL, ):
	def __init__(self,): 
		_TESTIMONIAL.__init__(self)
		self.name = "TESTIMONIALS"
		self.specie = 'nouns'
		self.basic = "testimonial"
		self.jsondata = {}
