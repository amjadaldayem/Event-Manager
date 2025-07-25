import React, { Component } from 'react';
import { Row, Col } from 'reactstrap';
import { Link } from 'react-router-dom';

class SummaryContainer extends Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <Col md="3">
        <Row>
          <Col md="2">
            <i className={this.props.iconName} />
          </Col>
          <Col md="10">
            {this.props.url === null ? (
              <p className="text-dark font-weight-light">
                {this.props.content}
              </p>
            ) : this.props.externalLink ? (
              <a href={this.props.url} target="blank">
                <p className="text-dark font-weight-light">
                  {this.props.content}
                </p>
              </a>
            ) : (
              <Link to={this.props.url}>
                <p className="text-dark font-weight-light">
                  {this.props.content}
                </p>
              </Link>
            )}
          </Col>
        </Row>
      </Col>
    );
  }
}
export default SummaryContainer;
